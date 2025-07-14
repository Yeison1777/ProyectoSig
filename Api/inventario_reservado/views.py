from django.shortcuts import render
from Api.inventario_reservado.serializer import InventarioReservadoSerializer
from Api.inventario_reservado.models import InventarioReservado
from rest_framework import viewsets


class InventarioReservadoViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = InventarioReservado.objects.all()  # Retrieve all records from the InventarioReservado model
    serializer_class = InventarioReservadoSerializer  # Use the InventarioReservadoSerializer for serialization