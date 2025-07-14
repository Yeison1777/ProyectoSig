from django.shortcuts import render
from Api.carrito.serializer import CarritoSerializer
from Api.carrito.models import Carrito
from rest_framework import viewsets

class CarritoViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Carrito.objects.all()  # Retrieve all records from the Carrito model
    serializer_class = CarritoSerializer  # Use the CarritoSerializer for serialization

# Create your views here.
