from django.shortcuts import render
from Api.detalle_carrito.serializer import DetalleCarritoSerializer
from Api.detalle_carrito.models import DetalleCarrito
from rest_framework import viewsets
# Create your views here.

class DetalleCarritoViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = DetalleCarrito.objects.all()  # Retrieve all records from the DetalleCarrito model
    serializer_class = DetalleCarritoSerializer  # Use the DetalleCarritoSerializer for serialization
    
