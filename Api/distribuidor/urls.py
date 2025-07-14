from django.urls import path, include
from rest_framework import routers
from Api.distribuidor import views

router = routers.DefaultRouter()
# Register the DistribuidorViewSet with the router
router.register(r'', views.DistribuidorViewSet, basename='distribuidor')
urlpatterns = [
    path('', include(router.urls))  # Include the router's URLs in the urlpatterns
]