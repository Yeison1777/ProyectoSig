from django.shortcuts import render
from rest_framework import viewsets
from Api.color.models import Color
from Api.color.serializer import ColorSerializer


# Create your views here.
class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
