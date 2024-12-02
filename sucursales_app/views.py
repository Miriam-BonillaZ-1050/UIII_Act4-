from django.shortcuts import render, redirect
from .models import Sucursales

# Vista de inicio, muestra todas las sucursales
def inicio_vista(request):
    sucursales = Sucursales.objects.all()
    return render(request, 'gestionarSucursales.html', {'missucursales': sucursales})

# Vista para registrar una nueva sucursal
def registrarSucursal(request):
    if request.method == "POST":
        id_sucursal = request.POST["num_id_sucursal"]
        nombre_suc = request.POST["txt_nombre_sucursal"]
        direccion_suc = request.POST["txt_direccion_sucursal"]
        ciudad = request.POST["txt_ciudad_sucursal"]
        telefono_suc = request.POST["txt_telefono_sucursal"]
        id_proveedor = request.POST["num_id_proveedor"]

        Sucursales.objects.create(
            id_sucursal=id_sucursal,
            nombre_suc=nombre_suc,
            direccion_suc=direccion_suc,
            ciudad=ciudad,
            telefono_suc=telefono_suc,
            id_proveedor=id_proveedor
        )
        return redirect('/')

    return render(request, "registrarSucursal.html")

# Vista para seleccionar una sucursal para editar
def seleccionarSucursal(request, id_sucursal):
    sucursal = Sucursales.objects.get(id_sucursal=id_sucursal)
    return render(request, "editarSucursal.html", {"sucursal": sucursal})

# Vista para editar los datos de una sucursal
def editarSucursal(request):
    if request.method == "POST":
        id_sucursal = request.POST["num_id_sucursal"]
        nombre_suc = request.POST["txt_nombre_sucursal"]
        direccion_suc = request.POST["txt_direccion_sucursal"]
        ciudad = request.POST["txt_ciudad_sucursal"]
        telefono_suc = request.POST["txt_telefono_sucursal"]
        id_proveedor = request.POST["num_id_proveedor"]

        sucursal = Sucursales.objects.get(id_sucursal=id_sucursal)
        sucursal.nombre_suc = nombre_suc
        sucursal.direccion_suc = direccion_suc
        sucursal.ciudad = ciudad
        sucursal.telefono_suc = telefono_suc
        sucursal.id_proveedor = id_proveedor
        sucursal.save()

        return redirect('/')

    return render(request, "editarSucursal.html")

# Vista para borrar una sucursal
def borrarSucursal(request, id_sucursal):
    sucursal = Sucursales.objects.get(id_sucursal=id_sucursal)
    sucursal.delete()
    return redirect("/")
