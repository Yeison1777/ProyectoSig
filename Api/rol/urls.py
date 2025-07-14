from django.urls import path, include
from Api.rol import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register(r'usuario', views.UsuarioViewSet)
router.register(r'', views.RolViewSet, basename='rol')
urlpatterns = [
    path ('', include(router.urls))
]
