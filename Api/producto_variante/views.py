from django.shortcuts import render
from Api.producto_variante.models import Producto_Variante
from Api.producto_variante.serializer import ProductoVarianteSerializer
from rest_framework import viewsets
# Create your views here.

class  ProductoVarianteViewSet(viewsets.ModelViewSet):
    queryset = Producto_Variante.objects.all()
    serializer_class = ProductoVarianteSerializer
