##############################################################################################################
##############################################################################################################
##############################################################################################################
####        CLASE PRODUCTO IMAGEN COLOR     ####

from django.db import models
from django.core.exceptions import ObjectDoesNotExist  # Importar para manejo específico de errores

from Api.producto.models import Producto
from Api.color.models import Color
from django.utils.translation import gettext_lazy as _

class ImagenProductoColor(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes_color')
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/color/')
    #es_principal = models.BooleanField(default=False)  # ¡Descomentado y necesario!
    #orden = models.PositiveIntegerField(default=0)  # Opcional: para ordenar imágenes

    class Meta:
        db_table = 'imagen_producto_color'
        # Removí unique_together para permitir múltiples imágenes por color
        #ordering = ['orden', 'es_principal']  # Ordena por prioridad

    #def __str__(self):
    #    return f"Imagen de {self.producto.nombre} - Color: {self.color.nombre}"