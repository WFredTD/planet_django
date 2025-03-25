# Description: Arquivo responsável por controlar as views da aplicação galeria

from django.shortcuts import render # Importando a função render, responsável por renderizar um modelo
from django.http import HttpResponse # Importando a função HttpResponse, responsável por retornar uma resposta HTTP

# função responsável pela página principal
def index(request):
    return render(request, 'galeria/index.html') # Renderiza o modelo index.html, entrando na pasta galeria e depois na pasta templates
