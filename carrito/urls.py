from django.urls import path
from . import views



urlpatterns = [
    path('carrito', views.index, name="carrito"),
    path("agregar/<int:comic_id>/", views.agregarCarro, name="agregar"),
    path("eliminar/<int:comic_id>/", views.eliminarCarro, name="eliminar"),
    path("restar/<int:comic_id>", views.restarCarro, name="restar"),
    path("limpiar/", views.limpiarCarro, name="limpiar"),
]
