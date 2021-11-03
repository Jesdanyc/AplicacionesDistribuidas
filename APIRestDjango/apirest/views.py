from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TrabajadorSerializer
from .models import Trabajador
from apirest import serializers

class TrabajadorViewSet (viewsets.ModelViewSet):
    queryset=Trabajador.objects.all();
    serializer_class=TrabajadorSerializer


# Create your views here.
