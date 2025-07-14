from django.shortcuts import render
from Api.direccion.serializer import DireccionSerializer
from Api.direccion.models import Direccion
from rest_framework import viewsets

# Create your views here.

class DireccionViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Direccion.objects.all()  # Retrieve all records from the Direccion model
    serializer_class = DireccionSerializer  # Use the DireccionSerializer for serialization
