from django.db import models

class Sucursales(models.Model):
    id_sucursal = models.CharField(primary_key=True, max_length=8)
    nombre_suc = models.CharField(max_length=100)
    direccion_suc = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono_suc = models.CharField(max_length=20)
    id_proveedor = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_suc} - {self.ciudad}"
