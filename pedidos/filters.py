import django_filters as filters

from .models import Cliente, Pedido


class PedidoFilter(filters.FilterSet):

    cliente = filters.CharFilter(method="search_cliente")
    data_pedido__gte = filters.DateTimeFilter(field_name="data_pedido", lookup_expr="gte")
    data_pedido__lte = filters.DateTimeFilter(field_name="data_pedido", lookup_expr="lte")
    
    def search_cliente(self, queryset, name, value):
        return queryset.filter(cliente__nome__icontains=value)

    class Meta:
        model = Pedido
        fields = "__all__"


class ClienteFilter(filters.FilterSet):
    nome = filters.CharFilter(
        field_name="nome", lookup_expr="icontains")
    cpf = filters.CharFilter(
        field_name="cpf", lookup_expr="icontains")

    class Meta:
        model = Cliente
        fields = [
            "nome",
            "cpf",
        ]
