from rest_framework import serializers
from Api.detalle_carrito.models import DetalleCarrito

class DetalleCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCarrito  # Model to work with
        fields = '__all__'  # Serialize all fields of the DetalleCarrito model