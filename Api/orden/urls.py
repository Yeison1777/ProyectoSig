from django.urls import path, include
from rest_framework import routers
from Api.orden import views 
from .views import obtener_ruta_optima

router = routers.DefaultRouter()
router.register(r'', views.OrdenViewSet, basename='orden')
urlpatterns = [
    path('', include(router.urls)),
    # ... otros endpoints ...
    #path('ruta-optima/', obtener_ruta_optima, name='ruta_optima'),
]




#urlpatterns = [
    
#]