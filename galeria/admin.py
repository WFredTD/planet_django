from django.contrib import admin
from . models import Fotografias # Importando o modelo Fotografias, responsável por criar a tabela no banco de dados

class FotografiasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'legenda', 'descricao', 'foto', 'publicada', 'data_fotografia') # Campos que serão exibidos na tabela do admin
    list_display_links = ('nome',"legenda") # Campos que serão pesquisáveis no admin
    search_fields = ('nome',) # Campos que serão pesquisáveis no admin
    list_filter = ('categoria',) # Campos que serão filtráveis no admin
    list_per_page = 3 # Número de itens por página no admin
    list_editable = ('publicada',) # Campos que podem ser editados diretamente na tabela do admin


admin.site.register(Fotografias, FotografiasAdmin) # Registra o modelo Fotografias no admin, com as configurações definidas na classe FotografiasAdmin