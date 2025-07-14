from rest_framework import serializers
from Api.vehiculo.models import Vehiculo
# lo que esta entre parentesis es la HERENCIA
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo  # MODELO CON QUE SE VA A TRABAJAR
        # fields = ('nombre_completo', 'nombre_usuario')  # CAMPOS QUE SE VAN A USAR DEL MODELO
        fields = '__all__'  # CON ESTE COMANDO SE HACE QUE SE SERIALICEN TODOS LOS CAMPOS DEL MODELO DE ARRIBA