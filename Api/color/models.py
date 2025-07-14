from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Color(models.Model):
   
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'color'  # Esto cambiará el nombre de la tabla
        default_permissions = ()  # Desactiva los permisos automáticos
        permissions = [
            ('crear_Color', _('Puede crear color')),
            ('editar_Color', _('Puede editar color')),
            ('eliminar_Color', _('Puede eliminar color')),
            ('ver_Color', _('Puede ver color')),
        ]
