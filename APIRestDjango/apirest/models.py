from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class Trabajador (models.Model):

    nombres=models.CharField(max_length=50)
    dni=models.CharField(max_length=8,null=True)
    celular=models.CharField(max_length=9)
    direccion=models.CharField(max_length=20,null=True)
    especialidad=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    area=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Trabajador")
        verbose_name_plural = ("Trabajadores")

    def __str__(self):
        return self.nombres