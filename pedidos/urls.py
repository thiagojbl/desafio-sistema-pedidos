from rest_framework import routers

from . import views

app_name = "pedidos"
router = routers.SimpleRouter()
router.register(r'produto', views.ProdutoViewSet, basename='produto')
router.register(r'cliente', views.ClienteViewSet, basename='cliente')
router.register(r'pedido', views.PedidoViewSet, basename='pedido')
urlpatterns = []
urlpatterns += router.urls
