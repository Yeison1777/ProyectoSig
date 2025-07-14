from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from Api.vehiculo.models import Vehiculo
from Api.distribuidor.models import Distribuidor

class VehiculoDistribuidor(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='vehiculo')
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE, related_name='distribuidor')
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'vehiculo_distribuidor'
        unique_together = ['vehiculo', 'distribuidor', 'activo']
        default_permissions = ()
        permissions = [
            ('crear_VehiculoDistribuidor', _('Puede crear asignación de vehículo')),
            ('editar_VehiculoDistribuidor', _('Puede editar asignación de vehículo')),
            ('eliminar_VehiculoDistribuidor', _('Puede eliminar asignación de vehículo')),
            ('ver_VehiculoDistribuidor', _('Puede ver asignación de vehículo')),
        ]

    def __str__(self):
        return f"{self.vehiculo.placa} - {self.distribuidor.user.get_full_name()}"