from django.urls import include, path
from Api.inventario import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'', views.InventarioViewSet, basename='inventario')
urlpatterns = [
    path ('', include(router.urls))
]