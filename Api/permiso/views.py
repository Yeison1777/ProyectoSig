from django.shortcuts import render
from django.contrib.auth.models import Permission
from Api.permiso.serializer import PermisoSerializer
from rest_framework import viewsets

# Create your views here.

class PermisoViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermisoSerializer
