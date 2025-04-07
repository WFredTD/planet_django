# Description: Arquivo responsável por controlar as views da aplicação galeria

from django.shortcuts import render, get_object_or_404 # Importando a função render, responsável por renderizar um modelo
from galeria.models import Fotografias # Importando o modelo Fotografias, responsável por criar a tabela no banco de dados
#from django.http import HttpResponse # Importando a função HttpResponse, responsável por retornar uma resposta HTTP, não utilizada no momento

# função responsável pela página principal
def index(request):
    # mock={
    #     1:{"nome":"Mercúrio",
    #     "legenda":"Planeta mais próximo do sol",},
    #     2:{"nome":"Neptuno",
    #     "legenda":"Planeta mais distante do sol",},
    #     3:{"nome":"Galaxia",
    #     "legenda":"Galáxia é um sistema de estrelas, poeira e gás que estão ligados pela gravidade",},
    #     4:{"nome":"Sol",
    #     "legenda":"Estrela central do sistema solar",},
    #     5:{"nome":"Lua",
    #     "legenda":"Satélite natural da Terra",},
    #     6:{"nome":"Vegeta",
    #     "legenda":"Planeta fictício do anime Dragon Ball",},
    # }
    # Acima temos dados mockados, ou seja, dados de teste, que não estão no banco de dados, mas são utilizados para testar a aplicação

    fotografias = Fotografias.objects.all()
    return render(request, 'galeria/index.html', {"cards":fotografias}) # Renderiza o modelo index.html, entrando na pasta galeria e depois na pasta templates

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografias, pk=foto_id) # get_object_or_404 é uma função que retorna um objeto ou 404 caso não encontre o objeto, pk é a chave primária do objeto
    return render(request, 'galeria/imagem.html', {'foto': fotografia}) # Renderiza o modelo imagem.html, passando o objeto foto como parâmetro

def contato(request):
    return render(request, 'galeria/contato.html')