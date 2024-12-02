from django.db import models

class Proveedores(models.Model):
    id_proveedor = models.CharField(primary_key=True, max_length=8)
    nombre_p = models.CharField(max_length=100)
    telefono_p = models.CharField(max_length=20)
    email_p = models.EmailField(max_length=100)
    direccion_p = models.CharField(max_length=200)
    ciudad_p = models.CharField(max_length=100)
    id_empleado = models.IntegerField()

    def __str__(self):
        return self.nombre_p
