from django.urls import path, include
from rest_framework import routers
from Api.detalle_carrito import views

router = routers.DefaultRouter()
# Register the CarritoViewSet with the router
router.register(r'', views.DetalleCarritoViewSet, basename='detalle_carrito')
urlpatterns = [
    path('', include(router.urls))  # Include the router's URLs in the urlpatterns
]
