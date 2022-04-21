from django.shortcuts import render

from .models import Curso


def index(request):
    cursos_cards = Curso.objects.all()
    
    context = {
        'cursos': cursos_cards
    }

    return render(request, "index.html", context)
