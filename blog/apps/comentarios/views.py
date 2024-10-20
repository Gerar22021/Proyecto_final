from typing import Any
from django.shortcuts import render
from .forms import ComentarioForm
from .models import Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models.query import QuerySet

def agregar_comentario(request):
    form = ComentarioForm(request.POST)
    if form.is_valid():
        form.save()
        form = ComentarioForm()

    template_name= 'articulos/agregar_comentario.html'
    context = {
        'form' : form,
    }

    return render(request, template_name, context)

""" def agregar_comentario(request):
    form = ComentarioForm(request.POST)
    if form.is_valid():
        form.save()
        form = ComentarioForm()

    template_name= 'articulos/agregar_comentario.html'
    context = {
        'form' : form,
    }

    return render(request, template_name, context) """

def listar_comentarios(request):
    comentarios = Comentario.object.all()
    template_name = 'articulos/listar_comentarios.html'
    context = {
    'comentarios' : comentarios,
    }
    return render(request, template_name, context)

class EditarComentario(LoginRequiredMixin, UpdateView):
    model = Comentario
    fields = ['texto',]
    template_name = 'articulos/agregar_comentario.html'
    success_url = reverse_lazy('apps.post:listar_articulos')

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return queryset.filter(usuario = self.request.user)

class EliminarComentario(LoginRequiredMixin, DeleteView):
    model = Comentario
    # template_name = 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('apps.post:listar_articulos')
