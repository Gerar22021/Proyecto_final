from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from apps.comentarios.forms import ComentarioForm
from apps.comentarios.models import Comentario
from .models import Articulo, Categoria
from django.core.paginator import Paginator

class ListarCategorias(ListView):
    model = Categoria
    template_name = 'articulos/listar_categorias.html'
    context_object_name = 'categorias'
    paginate_by = 3

    def get_context_data(self):
        context = super().get_context_data()
        categorias = Categoria.objects.all().distinct('nombre')
        context['categorias'] = categorias
        return context

# Create your views here.
class AgregarArticulo(CreateView):
    model = Articulo
    template_name = 'articulos/agregar_articulo.html'
    fields = ['titulo','subtitulo','texto','categoria','imagen']
    success_url = reverse_lazy('index')

class ActualizarArticulo(UpdateView):
    model = Articulo
    template_name = 'articulos/actualizar_articulo.html'
    fields = ['titulo','subtitulo','texto','categoria','imagen']
    success_url = reverse_lazy('apps.post:listar_articulos')

class EliminarArticulo(DeleteView):
    model = Articulo
    template_name = 'articulos/Eliminar_articulo.html'
    success_url = reverse_lazy('apps.post:listar_articulos')

class ListarArticulos(ListView):
    model = Articulo
    template_name = 'articulos/listar_articulos.html'
    context_object_name = 'articulos'
    paginate_by = 3

    def get_context_data(self):
        context = super().get_context_data()
        articulos = Articulo.objects.all()
        context['articulos'] = articulos
        return context

def articulo_individual(request,id):
    articulo = Articulo.objects.get(id = id)
    comentarios = Comentario.objects.filter(articulo = id)
    form = ComentarioForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.articulo = articulo
            aux.usuario = request.user
            aux.save()
            form = ComentarioForm()
        else:
            return redirect('apps.blog_auth:sesion')

    context= {
        "articulo": articulo,
        "form" : form, 
        "comentarios" : comentarios
    }
    template_name = "articulos/articulo_individual.html"

    return render(request, template_name=template_name,context=context)

def listar_articulo_por_categoria(request, categoria):
    categoria_db = Categoria.objects.filter(nombre = categoria)
    articulos = Articulo.objects.filter(categoria = categoria_db[0].id)
    # Paginación
    paginator = Paginator(articulos, 3)
    page_number = request.GET.get('page')
    articulos_paginados = paginator.get_page(page_number)

    template_name = 'articulos/listar_articulos.html'
    context = {
        'articulos' : articulos_paginados,
        'page_obj': articulos_paginados,
        'paginator': paginator,
        'is_paginated': paginator.num_pages > 1,
        
    }
    return render(request, template_name=template_name, context=context)

def ordenar_por(request):
    orden = request.GET.get('orden', ' ')
    articulos = None

    if orden == 'fecha':
        articulos = Articulo.objects.order_by('fecha')
    elif orden == 'titulo':
        articulos = Articulo.objects.order_by('titulo')
    else:
        articulos = Articulo.objects.all()

    paginator = Paginator(articulos, 3) 
    page_number = request.GET.get('page')  
    articulos_paginados = paginator.get_page(page_number)

    template_name = 'articulos/listar_articulos.html'
    context = {
        'articulos': articulos_paginados,
        'page_obj': articulos_paginados,
        'paginator': paginator,
        'is_paginated': paginator.num_pages > 1,
        
    }
    return render(request, template_name, context)