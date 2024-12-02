from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarEmpleado/", views.registrarEmpleado, name="registrarEmpleado"),
    path("seleccionarEmpleado/<id_empleado>", views.seleccionarEmpleado, name="seleccionarEmpleado"),
    path("editarEmpleado/", views.editarEmpleado, name="editarEmpleado"),
    path("borrarEmpleado/<id_empleado>", views.borrarEmpleado, name="borrarEmpleado"),
]
