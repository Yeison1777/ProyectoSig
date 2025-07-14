from django.db import models
from Api.carrito.models import Carrito
from Api.producto.models import Producto
from Api.producto_variante.models import Producto_Variante
#from Api.producto_variante.models import ProductoVariante
#from Api.detalle_inventario.models import DetalleInventario


# Create your models here.

class DetalleCarrito(models.Model): 
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='detalles_carrito')
    #producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='detalles')
    producto_variante = models.ForeignKey(Producto_Variante, on_delete=models.CASCADE, related_name='detalles_carrito', null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    #detalle_inventario = models.ForeignKey(DetalleInventario, on_delete=models.CASCADE, related_name='detalles', null=True, blank=True)

    class Meta:
        db_table = 'detalle_carrito'
        default_permissions = ()
        permissions = [
            ('crear_detalle_carrito', 'Puede crear detalle de carrito'),
            ('editar_detalle_carrito', 'Puede editar detalle de carrito'),
            ('eliminar_detalle_carrito', 'Puede eliminar detalle de carrito'),
            ('ver_detalle_carrito', 'Puede ver detalle de carrito'),
        ]
    #def __str__(self):
    #    return f"Detalle de Carrito {self.carrito.id} - Producto: {self.producto_variante.producto.descripcion} - Cantidad: {self.cantidad} - Precio Unitario: {self.precio_unitario}"
