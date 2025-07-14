from rest_framework import serializers
from Api.detalle_inventario.models import Detalle_Inventario

class Detalle_Inventario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_Inventario
        fields = "__all__"