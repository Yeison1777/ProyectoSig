from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

class Vehiculo(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=20, unique=True)
    capacidad_carga = models.IntegerField()
    tipo_vehiculo = models.CharField(max_length=50)
    anio = models.IntegerField()
    
    class Meta:
        db_table = 'vehiculo'
        default_permissions = ()
        permissions = [
            ('crear_Vehiculo', _('Puede crear vehículo')),
            ('editar_Vehiculo', _('Puede editar vehículo')),
            ('eliminar_Vehiculo', _('Puede eliminar vehículo')),
            ('ver_Vehiculo', _('Puede ver vehículo')),
        ]
        
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"