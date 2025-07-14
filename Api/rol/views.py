from django.shortcuts import render
from django.contrib.auth.models import Group
from Api.rol.serializer import RolSerializer
from rest_framework import viewsets

class RolViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = RolSerializer


# Create your views here.
