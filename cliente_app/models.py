from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=100)
    apellido_p = models.CharField(max_length=100)
    apellido_m = models.CharField(max_length=100)
    fecha = models.DateField() 
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
