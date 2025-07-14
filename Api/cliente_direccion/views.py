from django.shortcuts import render
from Api.cliente_direccion  import serializer
from Api.cliente_direccion.models import ClienteDireccion
from rest_framework import viewsets

# Create your views here.

class ClienteDireccionViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = ClienteDireccion.objects.all()  # Retrieve all records from the ClienteDireccion model
    serializer_class = serializer.ClienteDireccionSerializer  # Use the ClienteDireccionSerializer for serialization
