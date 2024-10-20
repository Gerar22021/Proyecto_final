from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def listar_articulos(request):
    return render(request, 'listar_articulos.html')

def agregar_comentario(request):
    return render(request, 'agregar_comentario.html')