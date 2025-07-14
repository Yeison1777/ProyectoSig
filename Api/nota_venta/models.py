from django.db import models
from Api.cliente.models import Cliente


# Create your models here.

class NotaVenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='notas_venta')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('pagada', 'Pagada'),
        ('cancelada', 'Cancelada')
    ])

    class Meta:
        db_table = 'nota_venta'
        default_permissions = ()
        permissions = [
            ('crear_nota_venta', 'Puede crear nota de venta'),
            ('editar_nota_venta', 'Puede editar nota de venta'),
            ('eliminar_nota_venta', 'Puede eliminar nota de venta'),
            ('ver_nota_venta', 'Puede ver nota de venta'),
        ]

    #def __str__(self):
    #    return f"Nota de Venta {self.id} - Cliente: {self.cliente.nombre} - Total: {self.total}"