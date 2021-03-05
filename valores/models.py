import uuid
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


class Valores_de_mercado(models.Model):
    valor = models.CharField(max_length=15, unique=True)

    #def __str__(self):
     #   return self.valor



class Empresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=100)
    simbolo = models.CharField(max_length=10)
    valores_de_mercado = models.ManyToManyField(Valores_de_mercado)
