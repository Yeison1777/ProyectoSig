from django.db import models
from Api.cliente.models import Cliente
from Api.direccion.models import Direccion
# Create your models here.

class ClienteDireccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='direcciones')
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, related_name='clientes')

    class Meta:
        db_table = 'cliente_direccion'
        default_permissions = ()
        permissions = [
            ('crear_ClienteDireccion', 'Puede crear cliente direccion'),
            ('editar_ClienteDireccion', 'Puede editar cliente direccion'),
            ('eliminar_ClienteDireccion', 'Puede eliminar cliente direccion'),
            ('ver_ClienteDireccion', 'Puede ver cliente direccion'), 
        ]
    def __str__(self):
        return f"{self.cliente} - {self.direccion}"