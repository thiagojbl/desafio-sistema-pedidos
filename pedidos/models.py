from django.db import models


class Produto(models.Model):
    descricao = models.CharField("Descrição", max_length=50)
    marca = models.CharField("Marca", max_length=30)
    valor = models.FloatField("Valor", blank=True, null=True)
    valor_compra = models.FloatField("Valor de Compra", blank=True, null=True)


class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=50)
    cpf = models.CharField("Cpf", max_length=14)


class Pedido(models.Model):
    data_pedido = models.DateTimeField(
        "Data", auto_now=True)
    cliente = models.ForeignKey(
        Cliente, verbose_name="Cliente", related_name="pedido_clientes",
        on_delete=models.CASCADE)
    itens = models.ManyToManyField(
        Produto, related_name="pedidos_itens", through="ProdutoPedido")

    # def faturamento_total(self):
    # return .get_total


class ProdutoPedido(models.Model):
    produto = models.ForeignKey(
        Produto, verbose_name="Produto", related_name="produtos",
        on_delete=models.CASCADE)
    pedido = models.ForeignKey(
        Pedido, verbose_name="Pedido", related_name="pedidos",
        on_delete=models.CASCADE)
    valor = models.FloatField("Valor")
    quantidade = models.IntegerField("Quantidade")

    @property
    def get_total(self):
        pedidos = self.objects.all()
        return sum((pedido.valor * pedido.quantidade) for pedido in pedidos)
