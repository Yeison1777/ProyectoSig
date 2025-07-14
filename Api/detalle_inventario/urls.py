from django.urls import path, include
from Api.detalle_inventario import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.Detall_Inventario_ViewSet, basename='detalleInventario')
urlpatterns = [
    path('', include(router.urls))
]