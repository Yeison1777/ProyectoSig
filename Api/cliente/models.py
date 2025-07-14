from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    telefono = models.CharField(max_length=20)
    #direccion = models.CharField(max_length=255)
    ci_nit = models.CharField(max_length=20, unique=True)
    #fecha_nacimiento = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'cliente'
        default_permissions = ()
        permissions = [
            ('crear_Cliente', _('Puede crear cliente')),
            ('editar_Cliente', _('Puede editar cliente')),
            ('eliminar_Cliente', _('Puede eliminar cliente')),
            ('ver_Cliente', _('Puede ver cliente')),
        ]

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.telefono}"
