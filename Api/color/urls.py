from django.urls import path, include
from rest_framework import routers
from Api.color import views

router = routers.DefaultRouter()
#router.register(r'color', views.ColorViewSet)
router.register(r'', views.ColorViewSet, basename='color')
urlpatterns = [
    path('', include(router.urls))
]