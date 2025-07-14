from rest_framework import serializers
from Api.inventario_reservado.models import InventarioReservado

class InventarioReservadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventarioReservado  # Model to work with
        fields = '__all__'  # Serialize all fields of the InventarioReservado model