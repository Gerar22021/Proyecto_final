from pyexpat.errors import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.contacto.forms import ContactoForm

# Create your views here.
class ContactoUsuario(CreateView):
    template_name = 'users/contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, 'consulta enviada.')
        return super().form_valid(form)