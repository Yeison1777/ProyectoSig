from django.urls import path, include
from Api.talla import views 
from rest_framework import routers

router = routers.DefaultRouter()
#router.register(r'talla', views.TallaViewSet)
router.register(r'', views.TallaViewSet, basename='talla')  # Ruta vacía

urlpatterns = [
    path ('', include(router.urls))
]
