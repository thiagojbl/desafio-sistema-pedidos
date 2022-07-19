from django.db.models import DecimalField, ExpressionWrapper, F
from django.db.models.aggregates import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pedidos.filters import ClienteFilter, PedidoFilter
from pedidos.models import Cliente, Pedido, Produto, ProdutoPedido
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
        return self.filter_queryset(self.queryset)


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backend = [DjangoFilterBackend]
    filterset_class = PedidoFilter

    def get_queryset(self):
        return self.filter_queryset(self.queryset)

    @action(methods=["get"], detail=False,  url_path=r'faturamento_total')
    def faturamento_total(self, request):
        total = ProdutoPedido.objects.annotate(faturamento=ExpressionWrapper(
            F('valor') * F('quantidade'), output_field=DecimalField()))
        faturamento_total = total.aggregate(total=Sum('faturamento'))
        payload = dict(faturamento_total=faturamento_total['total'])
        return Response(payload, status=200)

    @action(methods=["get"], detail=False,  url_path=r'lucro')
    def lucro(self, request):
        total_bruto = ProdutoPedido.objects.annotate(faturamento_bruto=ExpressionWrapper(
            F('valor') * F('quantidade'), output_field=DecimalField()))
        total_compra = ProdutoPedido.objects.annotate(faturamento_compra=ExpressionWrapper(
            F('produto__valor_compra') * F('quantidade'), output_field=DecimalField()))
        faturamento_bruto = total_bruto.aggregate(
            total_bruto=Sum('faturamento_bruto'))
        faturamento_compra = total_compra.aggregate(
            total_compra=Sum('faturamento_compra'))

        lucro = faturamento_bruto['total_bruto'] - \
            faturamento_compra['total_compra']

        payload = dict(lucro=lucro)

        return Response(payload, status=200)
