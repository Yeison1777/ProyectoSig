from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Api.imagen import views


router = DefaultRouter()
router.register(r'', views.ImagenProductoColorViewSet, basename='imagen-producto-color')

urlpatterns = [
    path('', include(router.urls)),
]