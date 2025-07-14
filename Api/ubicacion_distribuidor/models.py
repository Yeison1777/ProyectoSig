from django.db import models
from Api.distribuidor.models import Distribuidor

class UbicacionDistribuidor(models.Model):
    distribuidor = models.OneToOneField(Distribuidor, on_delete=models.CASCADE, related_name='ubicacion')
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ubicación de {self.distribuidor} - {self.latitud}, {self.longitud}"