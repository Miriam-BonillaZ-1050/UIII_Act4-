from django.db import models

# Modelo de Productos
class Productos(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    id_sucursal = models.IntegerField()  # Esto asumo que es un ID de sucursal, por lo que se hace un IntegerField

    def __str__(self):
        return self.nombre
