from django.contrib import admin
from . models import Fotografias # Importando o modelo Fotografias, responsável por criar a tabela no banco de dados

class FotografiasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'legenda', 'descricao', 'foto') # Campos que serão exibidos na tabela do admin
    search_fields = ('nome',"legenda") # Campos que serão pesquisáveis no admin
    list_filter = ('legenda', "nome") # Campos que serão filtráveis no admin

admin.site.register(Fotografias, FotografiasAdmin) # Registra o modelo Fotografias no admin, com as configurações definidas na classe FotografiasAdmin