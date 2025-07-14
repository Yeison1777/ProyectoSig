from django.shortcuts import render
from django.contrib.auth.models import User
from Api.usuario.serializer import UsuarioSerializer, UsuarioCreateSerializer, UsuarioUpdateSerializer
from rest_framework import viewsets

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        """
        Usar serializer diferente según la acción:
        - UsuarioSerializer: para listar y obtener detalles (sin password)
        - UsuarioCreateSerializer: para crear usuarios (con password)
        - UsuarioUpdateSerializer: para actualizar usuarios (password opcional)
        """
        if self.action == 'create':
            return UsuarioCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return UsuarioUpdateSerializer
        else:
            return UsuarioSerializer  # Para list, retrieve, etc.


# Create your views here.
