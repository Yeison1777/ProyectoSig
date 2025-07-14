from django.urls import path, include
from rest_framework import routers
from Api.detalle_nota_venta import views

router = routers.DefaultRouter()
# Register the DetalleNotaVentaViewSet with the router
router.register(r'', views.DetalleNotaVentaViewSet, basename='detalle_nota_venta')
urlpatterns = [
    path('', include(router.urls))  # Include the router's URLs in the urlpatterns
]
