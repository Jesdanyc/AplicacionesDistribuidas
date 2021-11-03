from rest_framework import serializers
from .models import Trabajador

class TrabajadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Trabajador
        fields=['nombres','dni','celular','direccion','especialidad','email','area']
        #fields ='__all__'