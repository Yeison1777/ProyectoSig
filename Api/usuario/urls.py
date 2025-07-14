from django.urls import path, include
from Api.usuario import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register(r'usuario', views.UsuarioViewSet)
router.register(r'', views.UsuarioViewSet, basename='usuario')
urlpatterns = [
    path ('', include(router.urls))
]
