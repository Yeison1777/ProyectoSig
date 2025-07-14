from django.urls import path, include
from rest_framework import routers
from Api.vehiculo_distribuidor import views

router = routers.DefaultRouter()
# router.register(r'vehiculo_distribuidor', views.VehiculoDistribuidorViewSet)  
router.register(r'', views.VehiculoDistribuidorViewSet, basename='vehiculo_distribuidor')
urlpatterns = [
    path('', include(router.urls))
]
