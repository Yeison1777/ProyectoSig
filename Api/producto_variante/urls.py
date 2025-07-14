from django.urls import path, include
from Api.producto_variante import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register(r'usuario', views.UsuarioViewSet)
router.register(r'', views.ProductoVarianteViewSet, basename='productoVariante')
urlpatterns = [
    path ('', include(router.urls))
]
