from django.db import models
from datetime import datetime

# Create your models here.
class Fotografias(models.Model):
    # Opções de categorias é uma lista constantante que contém as opções de categorias que podem ser escolhidas para a fotografia
    OPCOES_CATEGORIA = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALAXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')
    ]
    # string, max_length é o tamanho máximo da string, null é se pode ser nulo, blank é se pode ser vazio

    nome = models.CharField(max_length=100, null=False, blank=False) # Nome da fotografia
    legenda = models.CharField(max_length=150, null=False, blank=False) # Legenda da fotografia
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='') # Categoria da fotografia
    descricao = models.TextField(null=False, blank=False) # Descrição da fotografia
    # foto = models.CharField(max_length=100, null=False, blank=False) # Imagem da fotografia
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=False) # Imagem da fotografia, upload_to é o diretório onde a imagem será salva, no caso, na pasta galeria
    publicada = models.BooleanField(default=False) # Se a fotografia está publicada ou não
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False) # Data da fotografia, auto_now_add adiciona a data atual quando o objeto é criado

    def __str__(self):
        return f'Fotografia [nome={self.nome}]' # Retorna o nome da fotografia quando for chamado o objeto