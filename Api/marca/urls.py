from django.urls import path, include
from rest_framework import routers
from Api.marca import views


router = routers.DefaultRouter()
#router.register(r'marca', views.MarcaViewSet)
router.register(r'', views.MarcaViewSet, basename='marca')

urlpatterns = [
    path('', include(router.urls))
]