from rest_framework import serializers
from Api.vehiculo_distribuidor.models import VehiculoDistribuidor


class VehiculoDistribuidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculoDistribuidor
        fields = '__all__'
        #read_only_fields = ('id', 'activo')
        #extra_kwargs = {
        #    'vehiculo': {'required': True},
        #    'distribuidor': {'required': True}
        #}
