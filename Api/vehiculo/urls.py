from django.urls import path, include
from rest_framework import routers
from Api.vehiculo import views

router = routers.DefaultRouter()
# Register the DistribuidorViewSet with the router
router.register(r'', views.VehiculoViewSet, basename='vehiculo')
urlpatterns = [
    path('', include(router.urls))  # Include the router's URLs in the urlpatterns
]