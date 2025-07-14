from rest_framework import serializers
from Api.direccion.models import Direccion
class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion  # Model to work with
        fields = '__all__'  # Serialize all fields of the Direccion model