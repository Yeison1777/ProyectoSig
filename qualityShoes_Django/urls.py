"""
URL configuration for qualityShoes_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from Api.orden.views import obtener_ruta_optima

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path("api/v1/marca/", include("Api.marca.urls")),
    path("api/v1/talla/", include("Api.talla.urls")),
    path("api/v1/producto/", include("Api.producto.urls")),
    path("api/v1/color/", include("Api.color.urls")),
    path("api/v1/usuario/", include("Api.usuario.urls")),
    path("api/v1/rol/", include("Api.rol.urls")),
    path("api/v1/permiso/", include("Api.permiso.urls")),
    path("api/v1/productosvariante/", include("Api.producto_variante.urls")),
    path("api/v1/inventario/", include("Api.inventario.urls")),
    path("api/v1/detalleInventario/", include("Api.detalle_inventario.urls")),
    path("api/v1/imagen-producto-color/", include("Api.imagen.urls")),
    path("api/v1/distribuidor/", include("Api.distribuidor.urls")),
    path("api/v1/vehiculo/", include("Api.vehiculo.urls")),
    path("api/v1/vehiculo-distribuidor/", include("Api.vehiculo_distribuidor.urls")),
    path("api/v1/carrito/", include("Api.carrito.urls")),
    path("api/v1/detalle_carrito/", include("Api.detalle_carrito.urls")),
    path("api/v1/nota_venta/", include("Api.nota_venta.urls")),
    path("api/v1/detalle_nota_venta/", include("Api.detalle_nota_venta.urls")),
    path("api/v1/cliente/", include("Api.cliente.urls")),
    path("api/v1/direccion/", include("Api.direccion.urls")),
    path("api/v1/cliente_direccion/", include("Api.cliente_direccion.urls")),
    path("api/v1/inventario_reservado/", include("Api.inventario_reservado.urls")),
    path("api/v1/pago/", include("Api.pago.urls")),
    path("api/v1/ubicacion_distribuidor/", include("Api.ubicacion_distribuidor.urls")),
    path("api/v1/orden/", include("Api.orden.urls")),
    path('api/v1/ruta-optima/', obtener_ruta_optima, name='ruta_optima'),
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
