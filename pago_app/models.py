from django.db import models

class Pago(models.Model):
    id_pago = models.CharField(primary_key=True, max_length=8)
    fecha_venta = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50)
    descripcion_compra = models.CharField(max_length=255)
    id_producto = models.CharField(max_length=10)

    def __str__(self):
        return f"Pago {self.id_pago} - {self.tipo}"
