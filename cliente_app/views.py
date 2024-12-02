from django.shortcuts import render, redirect
from .models import Cliente
# Create your views here.

def inicio_vista(request):
    losclientes=Cliente.objects.all()
    return render(request, 'gestionarClientes.html',{'misclientes':losclientes})

def registrarCliente(request):
    id_cliente = request.POST["num_id_cliente"]
    nombre = request.POST["txt_nombre_cliente"]
    apellido_p = request.POST["txt_apellidop_cliente"]
    apellido_m = request.POST["txt_apellidom_cliente"]
    fecha = request.POST["date_fecha_cliente"]
    direccion = request.POST["txt_direccion_cliente"]
    telefono = request.POST["txt_telefono_cliente"]

    guardarCliente = Cliente.objects.create(id_cliente=id_cliente,nombre=nombre,
    apellido_p=apellido_p,apellido_m=apellido_m,fecha=fecha,direccion=direccion,telefono=telefono)
    return redirect('/')

def seleccionarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    return render(request, "editarCliente.html",{"misclientes":cliente})

def editarCliente(request):
    id_cliente = request.POST["num_id_cliente"]
    nombre = request.POST["txt_nombre_cliente"]
    apellido_p = request.POST["txt_apellidop_cliente"]
    apellido_m = request.POST["txt_apellidom_cliente"]
    fecha = request.POST["date_fecha_cliente"]
    direccion = request.POST["txt_direccion_cliente"]
    telefono = request.POST["txt_telefono_cliente"]
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre=nombre
    cliente.apellido_p=apellido_p
    cliente.apellido_m=apellido_m
    cliente.fecha=fecha
    cliente.direccion=direccion
    cliente.telefono=telefono
    cliente.save()
    return redirect('/')

def borrarCliente(request, id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("/")