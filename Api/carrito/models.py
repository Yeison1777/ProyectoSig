from django.db import models
from django.contrib.auth.models import User
from Api.cliente.models import Cliente


# Create your models here.

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cliente_carrito')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'carrito'
        default_permissions = ()
        permissions = [
            ('crear_carrito', 'Puede crear carrito'),
            ('editar_carrito', 'Puede editar carrito'),
            ('eliminar_carrito', 'Puede eliminar carrito'),
            ('ver_carrito', 'Puede ver carrito'),
        ]

    def __str__(self):
        return f"Carrito de {self.cliente.user.username} - Total: {self.total}"