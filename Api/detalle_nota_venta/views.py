from django.shortcuts import render
from Api.detalle_nota_venta.serializer import DetalleNotaVentaSerializer
from Api.detalle_nota_venta.models import DetalleNotaVenta
from rest_framework import viewsets

# Create your views here.

class DetalleNotaVentaViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = DetalleNotaVenta.objects.all()  # Retrieve all records from the DetalleNotaVenta model
    serializer_class = DetalleNotaVentaSerializer  # Use the DetalleNotaVentaSerializer for serialization

    def get_queryset(self):
        """
        Optionally restricts the returned details to a given nota venta,
        by filtering against a 'nota_venta' query parameter in the URL.
        """
        queryset = self.queryset
        nota_venta_id = self.request.query_params.get('nota_venta', None)
        if nota_venta_id is not None:
            queryset = queryset.filter(nota_venta__id=nota_venta_id)
        return queryset