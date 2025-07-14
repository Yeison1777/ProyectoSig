from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from Api.distribuidor.serializer import DistribuidorSerializer, DistribuidorCreateSerializer, DistribuidorUpdateSerializer
from Api.distribuidor.models import Distribuidor

class DistribuidorViewSet(viewsets.ModelViewSet):
    queryset = Distribuidor.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return DistribuidorCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return DistribuidorUpdateSerializer
        else:
            return DistribuidorSerializer

    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request):
        user = request.user
        try:
            distribuidor = Distribuidor.objects.get(user=user)
            serializer = self.get_serializer(distribuidor)
            return Response(serializer.data)
        except Distribuidor.DoesNotExist:
            return Response({'detail': 'No es distribuidor'}, status=status.HTTP_404_NOT_FOUND)
    
    #def get_serializer_class(self):
    #    """
    #    Usar serializer diferente según la acción:
    #    - DistribuidorSerializer: para listar y obtener detalles
    #    - DistribuidorCreateSerializer: para crear distribuidores (con usuario)
    #    - DistribuidorUpdateSerializer: para actualizar distribuidores
    #    """
    #    if self.action == 'create':
    #        return DistribuidorCreateSerializer
    #    elif self.action in ['update', 'partial_update']:
    #        return DistribuidorUpdateSerializer
    #    else:
    #        return DistribuidorSerializer  # Para list, retrieve, etc.

# Create your views here.
