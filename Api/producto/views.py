from django.shortcuts import render
from rest_framework import viewsets
from Api.producto.models import Producto
from Api.producto.serializer import PorductoSerializer


# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = PorductoSerializer
