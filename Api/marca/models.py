from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Marca (models.Model):
   
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'marca'  # Esto cambiará el nombre de la tabla
        default_permissions = ()  # Desactiva los permisos automáticos
        permissions = [
            ('crear_Marca', _('Puede crear marca')),
            ('editar_Marca', _('Puede editar marca')),
            ('eliminar_Marca', _('Puede eliminar marca')),
            ('ver_Marca', _('Puede ver marca')),
        ]