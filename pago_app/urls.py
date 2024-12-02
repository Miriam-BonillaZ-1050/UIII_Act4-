from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarPago/", views.registrarPago, name="registrarPago"),
    path("seleccionarPago/<id_pago>", views.seleccionarPago, name="seleccionarPago"),
    path("editarPago/", views.editarPago, name="editarPago"),
    path("borrarPago/<id_pago>", views.borrarPago, name="borrarPago"),
]
