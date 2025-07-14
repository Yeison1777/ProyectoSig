from django.db import models

# Create your models here.


class Talla (models.Model):
    numero = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'talla'  # Esto cambiará el nombre de la tabla