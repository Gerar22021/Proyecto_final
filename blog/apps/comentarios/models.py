from django.db import models
from apps.post.models import Articulo
from apps.blog_auth.models import Usuario

# Create your models here.
class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, default=1)
    texto = models.TextField(verbose_name='Comentario', )
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-fecha',)

    def __str__(self) -> str:
        return self.texto