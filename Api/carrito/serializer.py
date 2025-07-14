from rest_framework import serializers
from Api.carrito.models import Carrito

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito  # Model to work with
        fields = '__all__'  # Serialize all fields of the Carrito model