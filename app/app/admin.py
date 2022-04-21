from django.contrib import admin
from .models import Curso


class CursoAdmin(admin.ModelAdmin):
    list_display = ('curso_descricao', 'graduacao', 'modalidade', 'imagem', 'link_faesa')


admin.site.register(Curso, CursoAdmin)
