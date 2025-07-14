from django.urls import path, include
from rest_framework import routers
from Api.nota_venta import views

router = routers.DefaultRouter()
# Register the NotaVentaViewSet with the router
router.register(r'', views.NotaVentaViewSet, basename='nota_venta')
urlpatterns = [
    path('', include(router.urls))  # Include the router's URLs in the urlpatterns
]
