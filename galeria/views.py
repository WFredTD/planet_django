# Description: Arquivo responsável por controlar as views da aplicação galeria

from django.shortcuts import render, get_object_or_404 # Importando a função render, responsável por renderizar um modelo
from django.db.models import Q # Importando a função Q, responsável por criar consultas complexas no banco de dados
from galeria.models import Fotografias # Importando o modelo Fotografias, responsável por criar a tabela no banco de dados
from galeria.utils import remove_accents # Importando a função remove_accents, responsável por remover os acentos de uma string, para facilitar a busca no banco de dados

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
    #
    # fotografias = Fotografias.objects.all() # Retorna todas as fotografias do banco de dados, ou seja, todas as fotografias que estão cadastradas no banco de dados
    fotografia = Fotografias.objects.order_by('-data_fotografia').filter(publicada=True) # Retorna todas as fotografias do banco de dados, ordenadas pela data da fotografia, ou seja, as fotografias mais recentes aparecem primeiro, e filtra as fotografias que estão publicadas, ou seja, que estão visíveis para o público
    return render(request, 'galeria/index.html', {"cards":fotografia}) # Renderiza o modelo index.html, entrando na pasta galeria e depois na pasta templates

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografias, pk=foto_id) # get_object_or_404 é uma função que retorna um objeto ou 404 caso não encontre o objeto, pk é a chave primária do objeto
    return render(request, 'galeria/imagem.html', {'fotografias': fotografia}) # Renderiza o modelo imagem.html, passando o objeto foto como parâmetro

def contato(request):
    return render(request, 'galeria/contato.html')

def buscar(request):
    result= Fotografias.objects.order_by('data_fotografia').filter(publicada=True) 

    if 'search' in request.GET:
        query = request.GET['search']
        if query:
            result = result.filter(
                Q(nome__icontains=query) | # O operador | é utilizado para fazer uma consulta OR, ou seja, se o nome ou a legenda contiver a string que foi passada na busca, ele retorna o resultado
                Q(legenda__icontains=query))

    return render(request, 'galeria/buscar.html', {'cards':result})

def filtrar_categoria(request, categoria):
    categoria_normalized = remove_accents(categoria).upper()
    fotografias = Fotografias.objects.filter(
        publicada=True,
        categoria=categoria_normalized
    ).order_by('-data_fotografia')
    return render(request, 'galeria/index.html', {"cards": fotografias})