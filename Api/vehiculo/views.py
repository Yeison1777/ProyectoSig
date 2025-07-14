from django.shortcuts import render
from Api.vehiculo.serializer import VehiculoSerializer
from Api.vehiculo.models import Vehiculo
from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated

class VehiculoViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Vehiculo.objects.all()  # es como mostrar todos los datos de la tabla Vehiculo
    serializer_class = VehiculoSerializer


# Create your views here.
