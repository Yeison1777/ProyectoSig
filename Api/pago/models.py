from django.db import models
from Api.nota_venta.models import NotaVenta

class Pago(models.Model):
    METODO_PAGO_CHOICES = [
        ('qr', 'QR'),
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('stripe', 'Stripe'),  # Nuevo método
    ]
    
    ESTADO_PAGO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('proceso', 'En Proceso'),
        ('realizado', 'Realizado'),
        ('fallido', 'Fallido'),
        ('cancelado', 'Cancelado'),
        # Estados específicos de Stripe:
        ('requires_payment_method', 'Requiere Método de Pago'),
        ('requires_confirmation', 'Requiere Confirmación'),
        ('requires_action', 'Requiere Acción'),
        ('processing', 'Procesando'),
        ('succeeded', 'Exitoso'),
        ('canceled', 'Cancelado'),
    ]
    
    # Campos básicos
    nota_venta = models.OneToOneField(NotaVenta, on_delete=models.CASCADE, related_name='pago')
    metodo_pago = models.CharField(max_length=10, choices=METODO_PAGO_CHOICES)
    estado = models.CharField(max_length=30, choices=ESTADO_PAGO_CHOICES, default='pendiente')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    # Campos específicos por método
    referencia_qr = models.CharField(max_length=100, null=True, blank=True)
    comprobante_qr = models.ImageField(upload_to='pagos/qr/', null=True, blank=True)
    ultimos_digitos_tarjeta = models.CharField(max_length=4, null=True, blank=True)
    tipo_tarjeta = models.CharField(max_length=20, null=True, blank=True)
    
    # Campos específicos de Stripe
    stripe_payment_intent_id = models.CharField(max_length=255, null=True, blank=True)
    stripe_charge_id = models.CharField(max_length=255, null=True, blank=True)
    stripe_customer_id = models.CharField(max_length=255, null=True, blank=True)
    stripe_payment_method_id = models.CharField(max_length=255, null=True, blank=True)
    
    # Campos adicionales
    observaciones = models.TextField(blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)  # Para errores de Stripe
    
    class Meta:
        db_table = 'pago'
        
    def __str__(self):
        return f"Pago de NotaVenta {self.nota_venta.id} - {self.metodo_pago} - {self.estado}"
    
    @property
    def is_stripe_payment(self):
        return self.metodo_pago == 'stripe'
    
    @property
    def is_completed(self):
        return self.estado in ['realizado', 'succeeded']
    
    @property
    def is_failed(self):
        return self.estado in ['fallido', 'canceled']