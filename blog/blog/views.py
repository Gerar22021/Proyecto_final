from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def listar_articulos(request):
    return render(request, 'listar_articulos.html')