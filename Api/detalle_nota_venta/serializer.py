from rest_framework import serializers
from Api.detalle_nota_venta.models import DetalleNotaVenta

class DetalleNotaVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleNotaVenta  # Model to work with
        fields = '__all__'  # Serialize all fields of the model above

    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("La cantidad debe ser mayor que cero.")
        return value

    def validate_precio_unitario(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio unitario no puede ser negativo.")
        return value