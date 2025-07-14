from django.urls import path, include
from rest_framework import routers
from Api.inventario_reservado import views

router = routers.DefaultRouter()
# Register the InventarioReservadoViewSet with the router   
router.register(r'', views.InventarioReservadoViewSet, basename='inventario_reservado')
urlpatterns = [
    path('', include(router.urls))  # Include the router's URLs in the urlpatterns
]