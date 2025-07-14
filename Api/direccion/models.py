from django.db import models


# Create your models here.

class Direccion(models.Model):
    direccion = models.CharField(max_length=100, null=False, blank=False)
    latitud = models.DecimalField(
        max_digits=10,
        decimal_places=8,
        null=False,
        blank=False,
        verbose_name="Latitud"
    )
    longitud = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        null=False,
        blank=False,
        verbose_name="Longitud"
    )
    #numero = models.CharField(max_length=10, null=False, blank=False)
    #ciudad = models.CharField(max_length=50, null=False, blank=False)
    #estado = models.CharField(max_length=50, null=False, blank=False)
    #codigo_postal = models.CharField(max_length=10, null=False, blank=False)

    class Meta:
        db_table = "direccion"
        default_permissions = ()
        permissions = [
            ("crear_direccion", "Puede crear dirección"),
            ("editar_direccion", "Puede editar dirección"),
            ("eliminar_direccion", "Puede eliminar dirección"),
            ("ver_direccion", "Puede ver dirección"),
        ]