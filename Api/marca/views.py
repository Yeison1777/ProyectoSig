from django.shortcuts import render
from Api.marca.serializer import MarcaSerializer
from Api.marca.serializer import Marca
from rest_framework import viewsets
# Create your views here.



# O R M
# MAPEO OBJETO RELACIONAL

class MarcaViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Marca.objects.all()  #es como mostrar todos los datos de la tabla programador
    serializer_class = MarcaSerializer