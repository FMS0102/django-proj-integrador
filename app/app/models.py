from django.db import models


class Curso(models.Model):
    curso_descricao = models.CharField('Curso', max_length=200)
    graduacao = models.CharField('Graduação', max_length=200)
    modalidade = models.CharField('Modalidade', max_length=200)
    imagem = models.CharField('Caminho da Imagem', max_length=1000)
    link_faesa = models.CharField('Link Faesa', max_length=1000)

    def __str__(self):
        return self.curso_descricao
