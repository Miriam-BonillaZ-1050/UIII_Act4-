from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarProveedor/", views.registrarProveedor, name="registrarProveedor"),
    path("seleccionarProveedor/<id_proveedor>", views.seleccionarProveedor, name="seleccionarProveedor"),
    path("editarProveedor/", views.editarProveedor, name="editarProveedor"),
    path("borrarProveedor/<id_proveedor>", views.borrarProveedor, name="borrarProveedor"),
]
