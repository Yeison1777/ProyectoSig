from rest_framework import serializers
from Api.orden.models import Orden

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'
        read_only_fields = ('fecha_creacion', 'fecha_asignacion', 'fecha_entrega')
    
    def validate_estado(self, value):
        if value not in dict(Orden.ESTADO_CHOICES).keys():
            raise serializers.ValidationError("Estado inválido.")
        return value