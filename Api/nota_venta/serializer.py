from rest_framework import serializers
from Api.nota_venta.models import NotaVenta

class NotaVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaVenta  # Model to work with
        fields = '__all__'  # Serialize all fields of the model above

    def validate_total(self, value):
        if value < 0:
            raise serializers.ValidationError("El total no puede ser negativo.")
        return value

    def validate_estado(self, value):
        valid_states = ['pendiente', 'pagada', 'cancelada']
        if value not in valid_states:
            raise serializers.ValidationError(f"Estado debe ser uno de: {', '.join(valid_states)}")
        return value