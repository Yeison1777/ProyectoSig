from django.db import models
from Api.nota_venta.models import NotaVenta
from Api.distribuidor.models import Distribuidor  # Repartidor
from Api.direccion.models import Direccion

class Orden(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),         # Esperando asignación de repartidor
        ('asignada', 'Asignada'),           # Ya tiene repartidor asignado
        ('en_camino', 'En camino'),         # El repartidor está en ruta
        ('entregada', 'Entregada'),         # Pedido entregado al cliente
        ('cancelada', 'Cancelada'),         # Pedido cancelado
    ]

    nota_venta = models.OneToOneField(NotaVenta, on_delete=models.CASCADE, related_name='orden')
    repartidor = models.ForeignKey(Distribuidor, on_delete=models.SET_NULL, null=True, blank=True, related_name='ordenes')
    direccion_entrega = models.ForeignKey(Direccion, on_delete=models.PROTECT)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_asignacion = models.DateTimeField(null=True, blank=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    # Puedes agregar campos para tracking, comentarios, etc.

    #def __str__(self):
    #    return f"Orden {self.id} - {self.nota_venta.cliente} - Estado: {self.estado}"