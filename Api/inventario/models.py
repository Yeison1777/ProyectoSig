from django.db import models
from Api.producto.models import Producto
from django.utils.translation import gettext_lazy as _



# Create your models here.

class Inventario(models.Model):
    producto = models.ForeignKey(
        Producto, on_delete=models.SET_NULL, null=True, blank=True
    )
    #descripcion_producto = models.CharField(max_length=256)
    cantidad_total = models.IntegerField()

    class Meta:
        db_table = 'inventario'  # Esto cambiará el nombre de la tabla
        default_permissions = ()  # Desactiva los permisos automáticos
        permissions = [
            ('crear_Inventario', _('Puede crear Inventario')),
            ('editar_Inventario', _('Puede editar Inventario')),
            ('eliminar_Inventario', _('Puede eliminar Inventario')),
            ('ver_Inventario', _('Puede ver Inventario')),
        ]