from rest_framework import serializers
from Api.imagen.models import ImagenProductoColor

# Lo que está entre paréntesis es la HERENCIA
class ImagenProductoColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProductoColor  # MODELO CON EL QUE SE VA A TRABAJAR
        fields = '__all__'  # SERIALIZA TODOS LOS CAMPOS DEL MODELO