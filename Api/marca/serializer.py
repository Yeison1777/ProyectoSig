from rest_framework import serializers
from Api.marca.models import Marca

#lo que esta entre parentesis es la HERENCIA
class MarcaSerializer( serializers.ModelSerializer ) :
    class Meta:
        model = Marca  #MODELO CON QUE SE VA TRABAJAR
        #fields = ('nombre_completo', 'nombre_usuario')  #CAMPOS QUE SE VAN A USAR DEL MODELO 
        fields = '__all__'  #CON ESTE COMANDO SE HACE QUE SE SERIALIZEN TODOS LOS CAMPOS DEL MODELO DE ARRIBA