from django.shortcuts import render
from .models import Musica
# Removendo import json, pois não será usado se você utilizar |json_script nos templates
# import json # Mantenha se ainda usar json.dumps em alguma view antiga sem |json_script

# Create your views here.

def index(request):
    return render(request, 'siteProcura/index.html', {})

def info(request):
    return render(request, 'siteProcura/info.html', {})

# --- VIEWS DE BUSCA ---

def busca_sequencial(request):
  data_queryset = Musica.objects.all().values(
        'track_id', 
        'track_name', 
        'track_artist', 
        'playlist_genre',    # Correto
        'track_popularity',  # Correto
        'duration_ms',       # Correto
        'danceability'       # Opcional
    ).order_by('track_id')
  data_list = list(data_queryset) 
  
  context = {
    'dados_para_js': data_list, 
    'total_registros': len(data_list)
  }
  
  return render(request, 'siteProcura/busca_sequencial.html', context)

def busca_indexada(request):
    # Se você usar |json_script no template, remova o json.dumps
    # Se usar o método antigo (|escapejs), mantenha o json.dumps
    
    data_queryset = Musica.objects.all().values('track_id', 'track_name', 'track_artist').order_by('track_id')
    data_list = list(data_queryset) 
    
    # Opção RECOMENDADA (para usar |json_script no HTML)
    data_json = data_list 

    # Opção Antiga (se usar |escapejs, que pode falhar)
    # data_json = json.dumps(data_list) 

    context = {
        'dados_para_js': data_json,
        'total_registros': len(data_list)
    }
    # O nome do template é busca_indexada.html
    return render(request, 'siteProcura/busca_indexada.html', context)


def busca_por_hashmap(request):
    """ Envia o dataset de músicas (desordenado) como lista Python pura. """
    
    # Busca os campos importantes
    data_queryset = Musica.objects.all().values('track_id', 'track_name', 'track_artist', 'track_popularity')
    data_list = list(data_queryset) 
    
    # Passa a lista Python pura (data_list)
    # O template deve usar {{ dados_para_js|json_script:"spotify-data" }}
    context = {
        'dados_para_js': data_list, 
        'total_registros': len(data_list)
    }
    # O nome do template no seu sistema de arquivos é busca_por_hashmap.html
    return render(request, 'siteProcura/busca_por_hashmap.html', context)

def todas_as_musicas(request):
    """ Envia o dataset completo e desordenado para o template. """
    
    # Busca todos os campos importantes de todas as músicas
    data_queryset = Musica.objects.all().values('track_id', 'track_name', 'track_artist', 'track_popularity')
    data_list = list(data_queryset) 
    
    context = {
        'dados_para_js': data_list, # Lista Python pura
        'total_registros': len(data_list)
    }
    
    return render(request, 'siteProcura/todas_as_musicas.html', context)