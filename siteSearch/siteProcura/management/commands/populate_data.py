# siteProcura/management/commands/populate_data.py

import requests
import pandas as pd
from django.core.management.base import BaseCommand
from siteProcura.models import Musica
from django.db import transaction
from io import StringIO

class Command(BaseCommand):
    help = 'Baixa o dataset de músicas do Spotify e popula o banco de dados.'
    
    def handle(self, *args, **options):
        # URL do CSV
        CSV_URL = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv'

        self.stdout.write(self.style.WARNING('Limpando dados antigos...'))
        Musica.objects.all().delete()
        
        self.stdout.write(f'Baixando dados do CSV em {CSV_URL}...')
        
        try:
            # 1. Baixa o CSV
            response = requests.get(CSV_URL)
            response.raise_for_status() # Lança erro para status 4xx/5xx

            # 2. Carrega no Pandas
            data_io = StringIO(response.text)
            df = pd.read_csv(data_io)
            
            # 3. Limpeza/Preparação (Remove NaN, etc.)
            df = df.dropna(subset=['track_id', 'track_name', 'track_artist'])

            # 4. Cria a lista de objetos Musica
            musicas_para_criar = []
            
            # Garante que o track_id (chave) seja único, se houver duplicatas no CSV
            df = df.drop_duplicates(subset=['track_id'])
            
            total_count = len(df)
            self.stdout.write(f'Encontrados {total_count} registros válidos para importação.')

            for index, row in df.iterrows():
                musica = Musica(
                    track_id=row['track_id'],
                    track_name=row['track_name'],
                    track_artist=row['track_artist'],
                    duration_ms=row['duration_ms'], 
                    track_popularity=row['track_popularity'],
                    playlist_genre=row['playlist_genre'],
                    danceability=row['danceability']
                )
                musicas_para_criar.append(musica)
            
            # 5. Inserção em Lote (Performance)
            with transaction.atomic():
                Musica.objects.bulk_create(musicas_para_criar)
            
            self.stdout.write(self.style.SUCCESS(f'{total_count} Músicas do Spotify importadas com sucesso!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro durante a importação: {e}'))