from django.shortcuts import render
from .models import Musica


def index(request):
    return render(request, 'siteProcura/index.html', {})

def info(request):
    return render(request, 'siteProcura/info.html', {})


def busca_sequencial(request):
  data_queryset = Musica.objects.all().values(
        'track_id', 
        'track_name', 
        'track_artist', 
        'playlist_genre',    
        'track_popularity',  
        'duration_ms',       
        'danceability'       
    ).order_by('track_id')
  data_list = list(data_queryset) 
  
  context = {
    'dados_para_js': data_list, 
    'total_registros': len(data_list)
  }
  
  return render(request, 'siteProcura/busca_sequencial.html', context)


def busca_indexada(request):
    data_queryset = Musica.objects.all().values(
        'track_id', 
        'track_name', 
        'track_artist', 
        'playlist_genre', 
        'track_popularity'  
    ).order_by('track_id')
    
    data_list = list(data_queryset) 
    
    context = {
        'dados_para_js': data_list,  
        'total_registros': len(data_list)
    }
    
    return render(request, 'siteProcura/busca_indexada.html', context)

def busca_por_hashmap(request):
    """ Envia o dataset de músicas (desordenado) como lista Python pura. """
    
    data_queryset = Musica.objects.all().values('track_id', 'track_name', 'track_artist', 'track_popularity')
    data_list = list(data_queryset) 
    
    context = {
        'dados_para_js': data_list, 
        'total_registros': len(data_list)
    }
    return render(request, 'siteProcura/busca_por_hashmap.html', context)

def todas_as_musicas(request):
    """ Envia o dataset completo e desordenado para o template. """
    
    data_queryset = Musica.objects.all().values('track_id', 'track_name', 'track_artist', 'track_popularity')
    data_list = list(data_queryset) 
    
    context = {
        'dados_para_js': data_list, 
        'total_registros': len(data_list)
    }
    
    return render(request, 'siteProcura/todas_as_musicas.html', context)