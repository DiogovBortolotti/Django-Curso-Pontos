from django.db import models

from atracoes.models import Atracao
from avaliacoes.models import Avaliacoes
from comentarios.models import Comentario
from enderecos.models import Endereco

# Create your models here.


class DocIdentificacao(models.Model):
    descricao = models.CharField(max_length=100)


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=True)
    atracoes = models.ManyToManyField(Atracao)
    comentario = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacoes)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos',
                             height_field=None, width_field=None, max_length=None, null=True, blank=True)
    doc_identificacao = models.OneToOneField(
        DocIdentificacao, on_delete=models.CASCADE, null=True, blank=True)

    # pip install Pillow
    # python manage.py makemigrations --empty 0006_pontoturistico_foto -- remove  para o vazio
    # python manage.py makemigrations migrate 0006_pontoturistico_foto  -- migra pacote removido do vazio

    @property
    def descricao_completa2(self):
        return f'{self.nome} - {self.descricao} - DENTRO DA MODEL'

    def __str__(self):
        return self.nome
