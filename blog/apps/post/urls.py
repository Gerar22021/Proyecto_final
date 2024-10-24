from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import AgregarArticulo, ActualizarArticulo, EliminarArticulo, ListarArticulos, ListarCategorias, articulo_individual, listar_articulo_por_categoria, ordenar_por

app_name = 'apps.post'

urlpatterns = [
    
    path('agregar_articulo/', AgregarArticulo.as_view(), name = 'agregar_articulo'),
    path('actualizar_articulo/<int:pk>', ActualizarArticulo.as_view(), name = 'actualizar_articulo'),
    path('eliminar_articulo/<int:pk>', EliminarArticulo.as_view(), name = 'eliminar_articulo'),
    path('listar_articulos/', ListarArticulos.as_view(), name = 'listar_articulos'),
    path('listar_por_categoria/<str:categoria>', listar_articulo_por_categoria, name='listar_por_categoria'),
    path('listar_categorias/', ListarCategorias.as_view(), name='listar_categorias'),
    path('ordenar_por/', ordenar_por, name = 'ordenar_por'),
    path('articulo_individual/<int:id>', articulo_individual, name='articulo_individual')

]