from django.shortcuts import render, redirect
from .models import Empleados

# Vista de inicio, muestra todos los empleados
def inicio_vista(request):
    empleados = Empleados.objects.all()
    return render(request, 'gestionarEmpleado.html', {'misempleados': empleados})

# Vista para registrar un nuevo empleado
def registrarEmpleado(request):
    if request.method == "POST":
        id_empleado = request.POST["num_id_empleado"]
        nombre_emp = request.POST["txt_nombre_empleado"]
        apellidos_emp = request.POST["txt_apellidos_empleado"]
        telefono_emp = request.POST["txt_telefono_empleado"]
        email_emp = request.POST["txt_email_empleado"]
        puesto = request.POST["txt_puesto_empleado"]
        id_cliente = request.POST["num_id_cliente"]

        Empleados.objects.create(
            id_empleado=id_empleado,
            nombre_emp=nombre_emp,
            apellidos_emp=apellidos_emp,
            telefono_emp=telefono_emp,
            email_emp=email_emp,
            puesto=puesto,
            id_cliente=id_cliente
        )
        return redirect('/')

    return render(request, "registrarEmpleado.html")

# Vista para seleccionar un empleado para editar
def seleccionarEmpleado(request, id_empleado):
    empleado = Empleados.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmpleado.html", {"empleado": empleado})

# Vista para editar los datos de un empleado
def editarEmpleado(request):
    if request.method == "POST":
        id_empleado = request.POST["num_id_empleado"]
        nombre_emp = request.POST["txt_nombre_empleado"]
        apellidos_emp = request.POST["txt_apellidos_empleado"]
        telefono_emp = request.POST["txt_telefono_empleado"]
        email_emp = request.POST["txt_email_empleado"]
        puesto = request.POST["txt_puesto_empleado"]
        id_cliente = request.POST["num_id_cliente"]

        empleado = Empleados.objects.get(id_empleado=id_empleado)
        empleado.nombre_emp = nombre_emp
        empleado.apellidos_emp = apellidos_emp
        empleado.telefono_emp = telefono_emp
        empleado.email_emp = email_emp
        empleado.puesto = puesto
        empleado.id_cliente = id_cliente
        empleado.save()

        return redirect('/')

    return render(request, "editarEmpleado.html")

# Vista para borrar un empleado
def borrarEmpleado(request, id_empleado):
    empleado = Empleados.objects.get(id_empleado=id_empleado)
    empleado.delete()
    return redirect("/")
