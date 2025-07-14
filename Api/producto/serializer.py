from rest_framework import serializers
from Api.producto.models import Producto


class PorductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'