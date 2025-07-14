from django.urls import path, include
from rest_framework import routers
from Api.ubicacion_distribuidor import views


router = routers.DefaultRouter()
router.register(r'', views.UbicacionDistribuidorViewSet, basename='ubicacion_distribuidor')
urlpatterns = [
    path('', include(router.urls))
]