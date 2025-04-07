from django.db import models

# Create your models here.
class Fotografias(models.Model):

    # string, max_length é o tamanho máximo da string, null é se pode ser nulo, blank é se pode ser vazio

    nome = models.CharField(max_length=100, null=False, blank=False) # Nome da fotografia
    legenda = models.CharField(max_length=150, null=False, blank=False) # Legenda da fotografia
    descricao = models.TextField(null=False, blank=False) # Descrição da fotografia
    foto = models.CharField(max_length=100, null=False, blank=False) # Imagem da fotografia

    def __str__(self):
        return f'Fotografia [nome={self.nome}]' # Retorna o nome da fotografia quando for chamado o objeto