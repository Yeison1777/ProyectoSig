from django.urls import path, include
from rest_framework import routers
from Api.cliente_direccion import views

router = routers.DefaultRouter()
# Register the ClienteDireccionViewSet with the router
router.register(r'', views.ClienteDireccionViewSet, basename='cliente_direccion')
urlpatterns = [
    path('', include(router.urls))  # Include the router's URLs in the urlpatterns
]   