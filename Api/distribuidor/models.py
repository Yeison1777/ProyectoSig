from django.contrib.auth.models import User
from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

class Distribuidor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='distribuidor')
    carnet = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    licencia = models.CharField(max_length=50)

    class Meta:
        db_table = 'distribuidor'
        default_permissions = ()
        permissions = [
            ('crear_Distribuidor', _('Puede crear distribuidor')),
            ('editar_Distribuidor', _('Puede editar distribuidor')),
            ('eliminar_Distribuidor', _('Puede eliminar distribuidor')),
            ('ver_Distribuidor', _('Puede ver distribuidor')),
        ]
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.carnet}"
