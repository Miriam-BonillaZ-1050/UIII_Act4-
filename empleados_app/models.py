from django.db import models

class Empleados(models.Model):
    id_empleado = models.CharField(primary_key=True, max_length=8)
    nombre_emp = models.CharField(max_length=100)
    apellidos_emp = models.CharField(max_length=200)
    telefono_emp = models.CharField(max_length=20)
    email_emp = models.EmailField(max_length=100)
    puesto = models.CharField(max_length=100)
    id_cliente = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_emp} {self.apellidos_emp}"
