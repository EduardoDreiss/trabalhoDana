from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscaSequencial/', views.busca_sequencial, name = 'busca_sequencial'),
    path('buscaIndexada/', views.busca_indexada, name = 'busca_indexada'),
    path('buscaPorHashmap/', views.busca_por_hashmap, name = 'busca_por_hashmap'),
    path('info/', views.info, name = 'info'),
    path('todas_as_musicas/', views.todas_as_musicas, name='todas_as_musicas')
]