from rest_framework import serializers
from Api.pago.models import Pago

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago  # Model to work with
        fields = '__all__'  # Serialize all fields of the Pago model
    
    def validate(self, data):
        # Validar que el monto coincida con el total de la nota de venta
        nota_venta = data.get('nota_venta')
        monto = data.get('monto')
        
        if nota_venta and monto:
            if monto != nota_venta.total:
                raise serializers.ValidationError("El monto debe coincidir con el total de la venta")
        
        # Validar campos específicos según método de pago
        metodo_pago = data.get('metodo_pago')
        estado = data.get('estado', 'pendiente')
        
        if metodo_pago == 'qr':
            if not data.get('referencia_qr'):
                raise serializers.ValidationError("Referencia QR es requerida para pagos QR")
        elif metodo_pago == 'tarjeta':
            if not data.get('ultimos_digitos_tarjeta'):
                raise serializers.ValidationError("Últimos dígitos de tarjeta son requeridos")
        elif metodo_pago == 'efectivo':
            # Para pagos en efectivo, el estado suele ser 'realizado' inmediatamente
            if estado == 'pendiente':
                data['estado'] = 'realizado'
        elif metodo_pago == 'stripe':
            # Para Stripe, validar campos específicos
            if not data.get('stripe_payment_intent_id'):
                raise serializers.ValidationError("Payment Intent ID es requerido para pagos Stripe")
            
            # Estados válidos para Stripe
            estados_stripe_validos = [
                'requires_payment_method', 'requires_confirmation', 
                'requires_action', 'processing', 'succeeded', 'canceled'
            ]
            if estado not in estados_stripe_validos:
                data['estado'] = 'requires_payment_method'
        
        # Validar transiciones de estado
        if self.instance:  # Si es una actualización
            estado_anterior = self.instance.estado
            if estado_anterior in ['realizado', 'succeeded'] and estado not in ['realizado', 'succeeded']:
                raise serializers.ValidationError("No se puede cambiar el estado de un pago ya completado")
        
        return data
        