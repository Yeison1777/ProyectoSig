from rest_framework import serializers
from Api.cliente.models import Cliente
from Api.usuario.serializer import UsuarioSerializer, UsuarioUpdateSerializer

class ClienteSerializer(serializers.ModelSerializer):
    """Serializer para cliente con información del usuario (sin password)"""
    user = UsuarioSerializer(read_only=True)  # Solo lectura, sin password
    
    class Meta:
        model = Cliente
        fields = ['id', 'user', 'telefono', 'ci_nit']
        read_only_fields = ['id']

class ClienteCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear cliente con datos del usuario (password se encripta)"""
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=8)
    email = serializers.EmailField(write_only=True)
    first_name = serializers.CharField(write_only=True, required=False)
    last_name = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = Cliente
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'telefono', 'ci_nit']
    
    def create(self, validated_data):
        # Extraer datos del usuario
        user_data = {
            'username': validated_data.pop('username'),
            'password': validated_data.pop('password'),
            'email': validated_data.pop('email'),
        }
        
        # Agregar nombre si se proporciona
        if 'first_name' in validated_data:
            user_data['first_name'] = validated_data.pop('first_name')
        if 'last_name' in validated_data:
            user_data['last_name'] = validated_data.pop('last_name')
        
        # Crear usuario con contraseña encriptada
        from django.contrib.auth.models import User
        user = User.objects.create_user(**user_data)  # ← ENCRIPTA AUTOMÁTICAMENTE
        
        # Crear cliente
        cliente = Cliente.objects.create(user=user, **validated_data)
        return cliente

class ClienteUpdateSerializer(serializers.ModelSerializer):
    """Serializer para actualizar cliente (password opcional)"""
    user = UsuarioUpdateSerializer(required=False)
    
    class Meta:
        model = Cliente
        fields = ['user', 'telefono', 'ci_nit']
    
    def update(self, instance, validated_data):
        # Actualizar datos del usuario si se proporcionan
        if 'user' in validated_data:
            user_data = validated_data.pop('user')
            user = instance.user
            
            for attr, value in user_data.items():
                setattr(user, attr, value)
            user.save()
        
        # Actualizar datos del cliente
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance