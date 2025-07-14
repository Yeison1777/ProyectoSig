from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
import stripe
import json

from Api.pago.serializer import PagoSerializer
from Api.pago.models import Pago
from Api.nota_venta.models import NotaVenta

# Configurar Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

class PagoViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Pago.objects.all()  # Retrieve all records from the Pago model
    serializer_class = PagoSerializer  # Use the PagoSerializer for serialization
    
    @action(detail=False, methods=['post'])
    def create_payment_intent(self, request):
        """
        Crear un Payment Intent de Stripe
        """
        try:
            nota_venta_id = request.data.get('nota_venta_id')
            nota_venta = NotaVenta.objects.get(id=nota_venta_id)
            
            # Crear Payment Intent en Stripe
            payment_intent = stripe.PaymentIntent.create(
                amount=int(nota_venta.total * 100),  # Stripe usa centavos
                currency='usd',
                metadata={
                    'nota_venta_id': nota_venta_id,
                    'cliente_id': nota_venta.cliente.id
                }
            )
            
            # Crear registro de pago
            pago = Pago.objects.create(
                nota_venta=nota_venta,
                metodo_pago='stripe',
                monto=nota_venta.total,
                estado='requires_payment_method',
                stripe_payment_intent_id=payment_intent.id
            )
            
            return Response({
                'client_secret': payment_intent.client_secret,
                'payment_intent_id': payment_intent.id,
                'pago_id': pago.id
            })
            
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    @action(detail=True, methods=['post'])
    def confirm_payment(self, request, pk=None):
        """
        Confirmar un pago de Stripe
        """
        try:
            pago = self.get_object()
            
            if pago.metodo_pago != 'stripe':
                return Response(
                    {'error': 'Este pago no es de Stripe'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Aquí puedes agregar lógica adicional para confirmar el pago
            # Por ejemplo, verificar el estado en Stripe
            
            return Response({'message': 'Pago confirmado'})
            
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

@csrf_exempt
@require_http_methods(["POST"])
def stripe_webhook(request):
    """
    Webhook de Stripe para recibir notificaciones
    """
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return JsonResponse({'error': 'Invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError as e:
        return JsonResponse({'error': 'Invalid signature'}, status=400)
    
    # Manejar eventos de Stripe
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        pago = Pago.objects.get(stripe_payment_intent_id=payment_intent['id'])
        pago.estado = 'succeeded'
        pago.stripe_charge_id = payment_intent.get('latest_charge')
        pago.save()
        
        # Actualizar estado de la nota de venta
        nota_venta = pago.nota_venta
        nota_venta.estado = 'pagada'
        nota_venta.save()
        
    elif event['type'] == 'payment_intent.payment_failed':
        payment_intent = event['data']['object']
        pago = Pago.objects.get(stripe_payment_intent_id=payment_intent['id'])
        pago.estado = 'fallido'
        pago.error_message = payment_intent.get('last_payment_error', {}).get('message', '')
        pago.save()
    
    return JsonResponse({'status': 'success'})
    
