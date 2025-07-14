from django.db import models
from Api.producto_variante.models import Producto_Variante
from Api.nota_venta.models import NotaVenta


# Create your models here.

class DetalleNotaVenta(models.Model):
    nota_venta = models.ForeignKey(NotaVenta, on_delete=models.CASCADE, related_name='detalles_nota_venta')
    producto_variante = models.ForeignKey(Producto_Variante, on_delete=models.CASCADE, related_name='detalles_nota_venta')
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'detalle_nota_venta'
        default_permissions = ()
        permissions = [
            ('crear_detalle_nota_venta', 'Puede crear detalle de nota de venta'),
            ('editar_detalle_nota_venta', 'Puede editar detalle de nota de venta'),
            ('eliminar_detalle_nota_venta', 'Puede eliminar detalle de nota de venta'),
            ('ver_detalle_nota_venta', 'Puede ver detalle de nota de venta'),
        ]

    #def __str__(self):
    #    return f"Detalle Nota Venta {self.id} - Producto: {self.producto_variante.producto.descripcion} - Cantidad: {self.cantidad}"
