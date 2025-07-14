from django.shortcuts import render
from Api.talla.serializer import TallaSerializer
from Api.talla.models import Talla
from rest_framework import viewsets

# Create your views here.

class TallaViewSet(viewsets.ModelViewSet):

    queryset = Talla.objects.all()
    serializer_class = TallaSerializer