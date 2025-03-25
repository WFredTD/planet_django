# Descrição: Arquivo de configuração de URLs da aplicação galeria, responsável por controlar as URLs da aplicação galeria

from django.urls import path
from galeria.views import index

# Boa prática de programação: criar um arquivo urls.py para cada aplicação
urlpatterns = [ # urlpatterns é uma lista de paths, ou seja, URLs
    path('', index), 
]