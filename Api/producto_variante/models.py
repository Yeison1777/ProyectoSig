from django.db import models
from django.core.exceptions import ObjectDoesNotExist  # Importar para manejo específico de errores
from Api.talla.models import Talla
from Api.marca.models import Marca
from Api.producto.models import Producto
from Api.color.models import Color
from django.utils.translation import gettext_lazy as _

class Producto_Variante(models.Model):
    codigo_SKU = models.CharField(max_length=10, null=False, blank=False)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    talla = models.ForeignKey(Talla, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    precio_compra = models.FloatField(max_length=5, null=False, blank=False)

    

    class Meta:
        db_table = "producto_variante"
        default_permissions = ()
        permissions = [
            ("crear_Producto_Variante", _("Puede crear producto_variante")),
            ("editar_Producto_Variante", _("Puede editar producto_variante")),
            ("eliminar_Producto_Variante", _("Puede eliminar producto_variante")),
            ("ver_Producto_Variante", _("Puede ver producto_variante")),
        ]


    

    