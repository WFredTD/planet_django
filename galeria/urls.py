# Descrição: Arquivo de configuração de URLs da aplicação galeria, responsável por controlar as URLs da aplicação galeria

from django.urls import path
from galeria.views import index, imagem, contato

# Boa prática de programação: criar um arquivo urls.py para cada aplicação
urlpatterns = [ # urlpatterns é uma lista de paths, ou seja, URLs
    path('', index, name= 'index'), # path vazio, ou seja, a página inicial, chama a função index


    path('imagem/<int:foto_id>/', imagem, name= 'imagem'), # path imagem, chama a função imagem, passando o id da foto como parâmetro
    
    
    path('contato/', contato, name= 'contato'), # path contato, chama a função contato
]