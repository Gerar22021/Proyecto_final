from django.db import models
from apps.blog_auth.models import Usuario
from django.db.models.signals import post_save

class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    colaborador = models.BooleanField(default=False)
    miembro = models.BooleanField(default=True)
    invitado = models.BooleanField(default=False)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'
    
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

post_save.connect(crear_perfil, sender=Usuario)