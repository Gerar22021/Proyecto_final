from django.contrib import admin
from apps.blog_auth.signals import Perfil
from .models import Usuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Perfil)