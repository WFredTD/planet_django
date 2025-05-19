"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # Importando o módulo admin
from django.urls import path, include # Importando a função include e o módulo path
from galeria.views import index # Importando a view index da aplicação galeria
from django.conf import settings # Importando as configurações do Django, para verificar se o DEBUG está ativado ou não
from django.conf.urls.static import static # Importando a função static, responsável por servir arquivos estáticos durante o desenvolvimento


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')), # Incluindo as urls da aplicação galeria
    path('', include('usuarios.urls')),
]
# Abaixo temos a configuração para servir arquivos estáticos durante o desenvolvimento, ou seja, quando o DEBUG estiver ativado, ou seja, quando estivermos em modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionando as URLs estáticas à lista de URLs, ou seja, adicionando as URLs dos arquivos estáticos à lista de URLs


