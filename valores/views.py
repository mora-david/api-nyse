import requests
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from .models import Empresa, Valores_de_mercado
from rest_framework.viewsets import ModelViewSet
from .serializer import EmpresaSerializer, ValoresSerializer

import copy
from datetime import datetime, timedelta, date


class EmpresaViewSet(ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return LibroSerializerGet
    #     else:
    #         return LibroSerializer


    def create(self, request, *args, **kwargs):
        url = 'https://www.findata.co.nz/markets/NYSE/symbols/' + request.data['simbolo'][0] + '.htm'
        r = request.get(url)

        if not request.data['simbolo'][0] in r:
            return {'error':'el simbolo no se encuentra'}



        empresa = Empresa.objects.create(nombre=request.data['nombre'],descripcion=request.data['descripcion'],
                                  simbolo=request.data['simbolo'])

        valores = request.data['valores_de_mercado']
        valores = valores.split(',')
        if  len(valores) > 50:
            return Response ({'error':'se exedió el tamaño del arreglo'})

        val_fin = []
        for v in valores:
            try:
                val = Valores_de_mercado.objects.get(valor=v)
                val_fin.append(val.id)
            except:
                valExist = Valores_de_mercado.objects.create(valor=v)
                val_fin.append((valExist.id))


        empresa.valores_de_mercado.set(val_fin)
        empresa.save()

        return Response({'ok':'ok'})


class ValoresViewSet(ModelViewSet):
    serializer_class = ValoresSerializer
    queryset = Valores_de_mercado.objects.all()

