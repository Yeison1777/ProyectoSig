from django.urls import path, include
from rest_framework import routers
from Api.pago import views

router = routers.DefaultRouter()

# Register the PagoViewSet with the router
router.register(r'', views.PagoViewSet, basename='pago')

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs in the urlpatterns
    path('webhook/stripe/', views.stripe_webhook, name='stripe_webhook'),
] 