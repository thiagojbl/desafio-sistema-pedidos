from rest_framework import serializers

from .models import Cliente, Itens, Pedido, Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ItensSerializer(serializers.ModelSerializer):
    pedido = serializers.IntegerField(required=False)

    class Meta:
        model = Itens
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    total = serializers.FloatField(write_only=True, required=False)
    itens = serializers.IntegerField(required=False)

    class Meta:
        model = Pedido
        fields = '__all__'

    def create(self, validated_data):
        print('create aqui;....:  ', validated_data)
        total = 0
        itens = validated_data['itens']
        print('\n\nitend ...', itens, '\n\n\n')
        pedido = Pedido.objects.create(
            cliente=validated_data['cliente'])

        for item in itens:
            print('\n\nitem valor:  ', item['valor'], '\n\n\n')
            Itens.objects.create(pedido=pedido, **item)
            total += item['valor'] * item['quantidade']
        pedido.total = total
        pedido.save()
        return pedido

    # def create(self, validated_data):
    #     print('create aqui;....:  ', validated_data)
    #     total = 0
    #     itens = validated_data['itens']
    #     print('\n\nitend ...', itens, '\n\n\n')
    #     pedido = Pedido.objects.create(
    #         cliente=validated_data['cliente'])

    #     for item in itens:
    #         print('\n\nitem valor:  ', item['valor'], '\n\n\n')
    #         Itens.objects.create(pedido=pedido, **item)
    #         total += item['valor'] * item['quantidade']
    #     pedido.total = total
    #     pedido.save()
    #     return pedido

    # def to_representation(self, instance):
    #     return super().to_representation(instance)
