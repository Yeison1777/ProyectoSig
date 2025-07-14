from rest_framework import serializers
from Api.cliente_direccion.models import ClienteDireccion

class ClienteDireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteDireccion  # Model to work with
        fields = '__all__'  # Serialize all fields of the model above

    def create(self, validated_data):
        return ClienteDireccion.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cliente = validated_data.get('cliente', instance.cliente)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.save()
        return instance
    

