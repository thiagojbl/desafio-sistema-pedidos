from rest_framework import serializers

from .models import Cliente, Pedido, Produto, ProdutoPedido


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProdutoPedidoSerializer(serializers.ModelSerializer):
    # pedido = serializers.IntegerField(required=False)

    class Meta:
        model = ProdutoPedido
        fields = '__all__'
        extra_kwargs = {
            "pedido": {"write_only": True, "required": False},
        }


class PedidoSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    itens = ProdutoPedidoSerializer(many=True, write_only=True)

    def get_total(self, obj):
        pedidos = ProdutoPedido.objects.filter(pedido=obj)
        return sum((pedido.valor * pedido.quantidade) for pedido in pedidos)

    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'total', 'itens']

    def create(self, validated_data):
        itens = validated_data.pop('itens')
        pedido = Pedido.objects.create(
            cliente=validated_data['cliente'])
        for item in itens:
            ProdutoPedido.objects.create(pedido=pedido, **item)
        return pedido

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['itens'] = ProdutoPedidoSerializer(
            ProdutoPedido.objects.filter(pedido_id=instance.id), many=True).data

        data['cliente'] = ClienteSerializer(
            Cliente.objects.get(id=instance.cliente.pk), many=False).data
        return data
