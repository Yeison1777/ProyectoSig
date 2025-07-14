from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# from Api.usuario.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    # CAMBIO: Agregar campos para roles y permisos
    roles = serializers.SlugRelatedField(
        many=True, slug_field='name', source='groups', read_only=True
    )
    permisos = serializers.SlugRelatedField(
        many=True, slug_field='codename', source='user_permissions', read_only=True
    )

    """Serializer para lectura de usuarios (sin exponer password)"""
    class Meta:
        model = User
        # CAMBIO: Agregar 'roles' y 'permisos' a los fields
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',
            'is_active', 'date_joined', 'roles', 'permisos'  # CAMBIO
        ]
        read_only_fields = ['id', 'date_joined']

class UsuarioCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear usuarios (con password encriptado)"""
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
    def create(self, validated_data):
        # Encriptar contraseña al crear usuario
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)  # ← AQUÍ SE ENCRIPTA
        user.save()
        return user

class UsuarioUpdateSerializer(serializers.ModelSerializer):
    """Serializer para actualizar usuarios (password opcional)"""
    password = serializers.CharField(write_only=True, min_length=8, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
    def update(self, instance, validated_data):
        # Encriptar contraseña solo si se proporciona
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)  # ← AQUÍ SE ENCRIPTA
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance