from django.urls import path, include
from rest_framework import routers
from Api.direccion import views

router = routers.DefaultRouter()
# Register the DireccionViewSet with the router
router.register(r'', views.DireccionViewSet, basename='direccion')
urlpatterns = [
    path('', include(router.urls))  # Include the router's URLs in the urlpatterns
]