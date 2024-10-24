from django.urls import path
from .views import agregar_comentario, EliminarComentario, listar_comentarios, EditarComentario

app_name = 'apps.comentarios'

urlpatterns = [
    path('agregar_comentario/', agregar_comentario, name='agregar_comentario'),
    path('eliminar_comentario/<int:pk>', EliminarComentario.as_view(), name = 'eliminar_comentario'),
    path('listar_comentarios/', listar_comentarios, name = 'listar_comentarios'),
    path('editar_comentario/<int:pk>', EditarComentario.as_view(), name = 'editar_comentario')

]

