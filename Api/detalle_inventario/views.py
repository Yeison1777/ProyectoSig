from django.shortcuts import render
from rest_framework import viewsets
from Api.detalle_inventario.serializer import Detalle_Inventario_Serializer
from Api.detalle_inventario.models import Detalle_Inventario


# Create your views here.

class Detall_Inventario_ViewSet(viewsets.ModelViewSet):
    queryset = Detalle_Inventario.objects.all()
    serializer_class = Detalle_Inventario_Serializer
