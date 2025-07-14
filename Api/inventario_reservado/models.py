from django.db import models
from django.shortcuts import render
from Api.cliente.models import Cliente
from Api.detalle_inventario.models import Detalle_Inventario
from Api.producto_variante.models import Producto_Variante
# Create your views here.
class InventarioReservado(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='inventario_reservado')
    detalle_inventario = models.ForeignKey(Detalle_Inventario, on_delete=models.CASCADE, related_name='inventario_reservado', null=True, blank=True)
    producto_variante = models.ForeignKey(Producto_Variante, on_delete=models.CASCADE, related_name='inventario_reservado', null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'inventario_reservado'
        default_permissions = ()
        permissions = [
            ('crear_inventario_reservado', 'Puede crear inventario reservado'),
            ('editar_inventario_reservado', 'Puede editar inventario reservado'),
            ('eliminar_inventario_reservado', 'Puede eliminar inventario reservado'),
            ('ver_inventario_reservado', 'Puede ver inventario reservado'),
        ]

    #def __str__(self):
    #    return f"Inventario Reservado {self.id} - Cliente: {self.cliente.nombre} - Producto Variante: {self.producto_variante.descripcion} - Cantidad: {self.cantidad}"