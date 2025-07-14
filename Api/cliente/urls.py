from django.urls import path, include
from rest_framework import routers
from Api.cliente import views

router = routers.DefaultRouter()
# Register the ClienteViewSet with the router
router.register(r'', views.ClienteViewSet, basename='cliente') 
urlpatterns = [
    path('', include(router.urls))  # Include the router's URLs in the urlpatterns
]