from django.urls import path, include
from rest_framework import routers
from Api.carrito import views

router = routers.DefaultRouter()
# Register the CarritoViewSet with the router
router.register(r'', views.CarritoViewSet, basename='carrito')
urlpatterns = [
    path('', include(router.urls))  # Include the router's URLs in the urlpatterns
]