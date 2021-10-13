from django.shortcuts import render
from .models import Curso

def index (request):
    dados = Curso.objects.all().filter(
        mostrar=True
    )
    return render(request,'home/index.html',{'dados':dados})

def mostrar(request, idbusca):
    dados = Curso.objects.get(id=idbusca)
    return render(request, 'home/detcurso.html', {'dados': dados})
