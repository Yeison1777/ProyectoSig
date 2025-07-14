from django.shortcuts import render
from Api.vehiculo_distribuidor.serializer import VehiculoDistribuidorSerializer
from Api.vehiculo_distribuidor.models import VehiculoDistribuidor
from rest_framework import viewsets

class VehiculoDistribuidorViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = VehiculoDistribuidor.objects.all()  # This retrieves all records from the VehiculoDistribuidor table
    serializer_class = VehiculoDistribuidorSerializer   
# Create your views here.
