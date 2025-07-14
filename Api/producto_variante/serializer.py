from rest_framework import serializers
from Api.producto_variante.models import Producto_Variante

class ProductoVarianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto_Variante
        fields = "__all__"