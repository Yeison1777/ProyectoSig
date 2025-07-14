from rest_framework import serializers
from Api.ubicacion_distribuidor.models import UbicacionDistribuidor

class UbicacionDistribuidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UbicacionDistribuidor
        fields = "__all__"
        read_only_fields = ('ultima_actualizacion',)  # Make 'ultima_actualizacion' read-only