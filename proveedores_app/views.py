from django.shortcuts import render, redirect
from .models import Proveedores

# Vista de inicio, muestra todos los proveedores
def inicio_vista(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'gestionarProveedor.html', {'misproveedores': proveedores})

# Vista para registrar un nuevo proveedor
def registrarProveedor(request):
    if request.method == "POST":
        id_proveedor = request.POST["num_id_proveedor"]
        nombre_p = request.POST["txt_nombre_proveedor"]
        telefono_p = request.POST["txt_telefono_proveedor"]
        email_p = request.POST["txt_email_proveedor"]
        direccion_p = request.POST["txt_direccion_proveedor"]
        ciudad_p = request.POST["txt_ciudad_proveedor"]
        id_empleado = request.POST["num_id_empleado"]

        Proveedores.objects.create(
            id_proveedor=id_proveedor,
            nombre_p=nombre_p,
            telefono_p=telefono_p,
            email_p=email_p,
            direccion_p=direccion_p,
            ciudad_p=ciudad_p,
            id_empleado=id_empleado
        )
        return redirect('/')

    return render(request, "registrarProveedor.html")

# Vista para seleccionar un proveedor para editar
def seleccionarProveedor(request, id_proveedor):
    proveedor = Proveedores.objects.get(id_proveedor=id_proveedor)
    return render(request, "editarProveedor.html", {"proveedor": proveedor})

# Vista para editar los datos de un proveedor
def editarProveedor(request):
    if request.method == "POST":
        id_proveedor = request.POST["num_id_proveedor"]
        nombre_p = request.POST["txt_nombre_proveedor"]
        telefono_p = request.POST["txt_telefono_proveedor"]
        email_p = request.POST["txt_email_proveedor"]
        direccion_p = request.POST["txt_direccion_proveedor"]
        ciudad_p = request.POST["txt_ciudad_proveedor"]
        id_empleado = request.POST["num_id_empleado"]

        proveedor = Proveedores.objects.get(id_proveedor=id_proveedor)
        proveedor.nombre_p = nombre_p
        proveedor.telefono_p = telefono_p
        proveedor.email_p = email_p
        proveedor.direccion_p = direccion_p
        proveedor.ciudad_p = ciudad_p
        proveedor.id_empleado = id_empleado
        proveedor.save()

        return redirect('/')

    return render(request, "editarProveedor.html")

# Vista para borrar un proveedor
def borrarProveedor(request, id_proveedor):
    proveedor = Proveedores.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()
    return redirect("/")
