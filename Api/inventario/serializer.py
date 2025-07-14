from rest_framework import serializers
from Api.inventario.models import Inventario


class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = "__all__"