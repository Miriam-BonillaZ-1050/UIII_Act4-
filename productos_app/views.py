from django.shortcuts import render, redirect
from .models import Productos  # Importar el modelo correcto

# Vista de inicio
def inicio_vista(request):
    productos = Productos.objects.all()
    return render(request, 'gestionarProductos.html', {'misproductos': productos})

# Vista para registrar un producto
def registrarProducto(request):
    id_producto = request.POST["num_id_producto"]
    nombre = request.POST["txt_nombre_producto"]
    descripcion = request.POST["txt_descripcion_producto"]
    stock = request.POST["num_stock_producto"]
    precio = request.POST["num_precio_producto"]
    categoria = request.POST["txt_categoria_producto"]
    id_sucursal = request.POST["num_id_sucursal"]

    Productos.objects.create(
        id_producto=id_producto,
        nombre=nombre,
        descripcion=descripcion,
        stock=stock,
        precio=precio,
        categoria=categoria,
        id_sucursal=id_sucursal
    )
    return redirect('/')

# Vista para seleccionar un producto para editar
def seleccionarProducto(request, id_producto):
    producto = Productos.objects.get(id_producto=id_producto)
    return render(request, "editarProductos.html", {"producto": producto})

# Vista para editar un producto
def editarProducto(request):
    id_producto = request.POST["num_id_producto"]
    nombre = request.POST["txt_nombre_producto"]
    descripcion = request.POST["txt_descripcion_producto"]
    stock = request.POST["num_stock_producto"]
    precio = request.POST["num_precio_producto"]
    categoria = request.POST["txt_categoria_producto"]
    id_sucursal = request.POST["num_id_sucursal"]

    producto = Productos.objects.get(id_producto=id_producto)
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.stock = stock
    producto.precio = precio
    producto.categoria = categoria
    producto.id_sucursal = id_sucursal
    producto.save()

    return redirect('/')

# Vista para borrar un producto
def borrarProducto(request, id_producto):
    producto = Productos.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect("/")
