from django.shortcuts import render
from Api.inventario.serializer import InventarioSerializer
from Api.inventario.models import Inventario
from rest_framework import viewsets

# Create your views here.

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
