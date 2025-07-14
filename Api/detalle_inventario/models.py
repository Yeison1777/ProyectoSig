from django.db import models
from Api.inventario.models import Inventario
from Api.producto.models import Producto
from Api.producto_variante.models import Producto_Variante
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Detalle_Inventario(models.Model):
    inventario = models.ForeignKey(
        Inventario, on_delete=models.SET_NULL, null=True, blank=True
    )
    producto_variante = models.ForeignKey(
        Producto_Variante, on_delete=models.SET_NULL, null=True, blank=True
    )
    cantidad = models.IntegerField(null=True, blank=False)
    precio_venta = models.DecimalField(
        max_digits=5,  # Máximo 10 dígitos en total (incluyendo decimales)
        decimal_places=2,
    )

    class Meta:
        db_table = 'detalle_inventario'  # Esto cambiará el nombre de la tabla
        default_permissions = ()  # Desactiva los permisos automáticos
        permissions = [
            ('crear_detalle_inventario', _('Puede crear detalle_inventario')),
            ('editar_detalle_inventario', _('Puede editar detalle_inventario')),
            ('eliminar_detalle_inventario', _('Puede eliminar detalle_inventario')),
            ('ver_detalle_inventario', _('Puede ver detalle_inventario')),
        ]
        