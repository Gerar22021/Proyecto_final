from django.shortcuts import render

def index(request):
    categorias = listar_categorias
    return render(request, 'index.html')

def acerca_de(request):
    return render(request, 'acercade.html')

def listar_categorias(request):
    return render(request, 'listar_categorias.html')

def listar_articulos(request):
    return render(request, 'listar_articulos.html')

def agregar_comentario(request):
    return render(request, 'agregar_comentario.html')