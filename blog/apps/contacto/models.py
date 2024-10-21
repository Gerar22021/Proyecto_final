from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_apellido