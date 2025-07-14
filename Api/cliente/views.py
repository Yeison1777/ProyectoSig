from django.shortcuts import render
from Api.cliente.serializer import ClienteSerializer, ClienteCreateSerializer, ClienteUpdateSerializer
from Api.cliente.models import Cliente
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()  # Retrieve all records from the Cliente model
    
    def get_serializer_class(self):
        """
        Usar serializer diferente según la acción:
        - ClienteSerializer: para listar y obtener detalles
        - ClienteCreateSerializer: para crear clientes (con usuario)
        - ClienteUpdateSerializer: para actualizar clientes
        """
        if self.action == 'create':
            return ClienteCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return ClienteUpdateSerializer
        else:
            return ClienteSerializer  # Para list, retrieve, etc.
        
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        try:
            cliente = Cliente.objects.get(user=request.user)
        except Cliente.DoesNotExist:
            return Response({'detail': 'No existe cliente para este usuario.'}, status=404)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
