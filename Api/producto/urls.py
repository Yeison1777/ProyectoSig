from django.urls import path, include
from rest_framework import routers
from Api.producto import views


router = routers.DefaultRouter()
#router.register(r'producto', views.ProductoViewSet)
router.register(r'', views.ProductoViewSet, basename='producto')  # Ruta vacía

urlpatterns = [
    path('', include(router.urls))
]