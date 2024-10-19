from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Articulo, Categoria
from django.core.paginator import Paginator

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
    
def listar_articulo_por_categoria(request, categoria):
    categoria_db = Categoria.objects.filter(nombre = categoria)
    libros = Articulo.objects.filter(categoria = categoria_db[0].id)
    # Paginación
    paginator = Paginator(Articulo, 3)
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