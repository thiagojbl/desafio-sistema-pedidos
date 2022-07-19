from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pedidos.filters import ClienteFilter, PedidoFilter
from pedidos.models import Cliente, Pedido, Produto
from pedidos.serializers import (ClienteSerializer, PedidoSerializer,
                                 ProdutoSerializer)


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backend = [DjangoFilterBackend]


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backend = [DjangoFilterBackend]
    filterset_class = ClienteFilter

    def get_queryset(self):
        print('get_queryset')
        return self.filter_queryset(self.queryset)


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backend = [DjangoFilterBackend]
    filterset_class = PedidoFilter

    def get_queryset(self):
        print('get_queryset')
        return self.filter_queryset(self.queryset)
