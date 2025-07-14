from django.shortcuts import render
from Api.nota_venta.serializer import NotaVentaSerializer
from Api.nota_venta.models import NotaVenta
from rest_framework import viewsets
# Create your views here.

class NotaVentaViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = NotaVenta.objects.all()  # Retrieve all records from the NotaVenta model
    serializer_class = NotaVentaSerializer  # Use the NotaVentaSerializer for serialization

    #def get_queryset(self):
    #    """
    #    Optionally restricts the returned notes to a given cliente,
    #    by filtering against a 'cliente' query parameter in the URL.
    #    """
    #    queryset = self.queryset
    #    cliente_id = self.request.query_params.get('cliente', None)
    #    if cliente_id is not None:
    #        queryset = queryset.filter(cliente__id=cliente_id)
    #    return queryset
