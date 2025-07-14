from rest_framework import serializers
from Api.talla.models import Talla

class TallaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Talla
        fields = '__all__'