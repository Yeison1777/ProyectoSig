from django.db import models
from Api.talla.models import Talla
from Api.marca.models import Marca
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Producto(models.Model):
    

    nombre = models.CharField(max_length=100)
   
    descripcion = models.CharField(max_length=256)

    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True)
    #talla = models.ForeignKey(Talla, on_delete=models.SET_NULL, null=True, blank=True)

        # Campo para una imagen principal (opcional)
    #imagen_principal = models.ImageField(
    #    upload_to='productos/',  # Carpeta donde se guardarán las imágenes
    #    null=True,
    #    blank=True
    #)
    class Meta:
        db_table = 'producto'  # Esto cambiará el nombre de la tabla
        default_permissions = ()  # Desactiva los permisos automáticos
        permissions = [
            ('crear_Productos', _('Puede crear productos')),
            ('editar_Productos', _('Puede editar productos')),
            ('eliminar_Productos', _('Puede eliminar productos')),
            ('ver_Productos', _('Puede ver productos')),
        ]
        