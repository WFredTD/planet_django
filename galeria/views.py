from django.shortcuts import render
from django.http import HttpResponse

# função responsável pela página principal
def index(request):
    return HttpResponse('<h1>Olá, Planetário!</h1>')
