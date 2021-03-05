
from rest_framework import serializers
from .models import Valores_de_mercado,Empresa

class ValoresSerializer(serializers.ModelSerializer):
    valor = serializers.SerializerMethodField()
    class Meta:
        model = Valores_de_mercado
        fields = ('valor',)


    def get_valor(self, obj):
        valores = []
        val = Valores_de_mercado.objects.filter(valor=obj.valor)
        for v in val:
            valores.append(v.valor)
        return valores




class EmpresaSerializer(serializers.ModelSerializer):
    #valores_de_mercado = ValoresSerializer(many=True, read_only=True)
    valores_de_mercado = serializers.SerializerMethodField()
    class Meta:
        model = Empresa
        fields = ('id','nombre','descripcion', 'simbolo', 'valores_de_mercado', )

    # def get_valores_de_mercado(self, obj):
    #     arr =[]
    #     for o in obj.valores_de_mercado:
    #         arr.append(o.valor)
    #
    #     return arr
    def get_valores_de_mercado(self, obj):
        valores = []
        for ob in obj.valores_de_mercado.all():
            valores.append(ob.valor)

        return valores







    #
    # def get_emisor(self, obj):
    #     return obj.prestamos.username
    #
    # def get_receptor(self, obj):
    #     return obj.prestamos.username
    #
    # def get_fecha(self, obj):
    #     return obj.fecha_prestamo
    #
    # def get_entregado(self, obj):
    #     return obj.prestado


