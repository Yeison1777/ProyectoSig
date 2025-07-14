from django.shortcuts import render
from Api.ubicacion_distribuidor.serializer import UbicacionDistribuidorSerializer
from Api.ubicacion_distribuidor.models import UbicacionDistribuidor
from rest_framework import viewsets
# Create your views here.

class UbicacionDistribuidorViewSet(viewsets.ModelViewSet):
    queryset = UbicacionDistribuidor.objects.all()
    serializer_class = UbicacionDistribuidorSerializer