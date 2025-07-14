from django.shortcuts import render
from Api.orden.serializer import OrdenSerializer
from Api.orden.models import Orden
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Api.orden.services import calcular_ruta_optima

# Create your views here.

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Aquí puedes agregar lógica adicional para filtrar o modificar el queryset si es necesario
        return queryset

    def perform_create(self, serializer):
        # Aquí puedes agregar lógica adicional antes de guardar la instancia
        serializer.save()  # Guarda la instancia del modelo




@api_view(['POST'])
#def obtener_ruta_optima(request):
#    origen = request.data.get('origen')
#    destinos = request.data.get('destinos', [])
#    resultado = calcular_ruta_optima(origen, destinos)
    # Extraer la lista de puntos de la respuesta de Google
#    puntos = []
#    try:
#        steps = resultado['routes'][0]['legs'][0]['steps']
#        for step in steps:
#            lat = step['start_location']['lat']
#            lng = step['start_location']['lng']
#            puntos.append(f"{lat},{lng}")
        # Agrega el último punto (destino final)
#        lat = steps[-1]['end_location']['lat']
#        lng = steps[-1]['end_location']['lng']
#        puntos.append(f"{lat},{lng}")
#    except Exception as e:
#        return Response({'error': f'No se pudo calcular la ruta: {e}'}, status=500)
#    return Response(puntos)
def obtener_ruta_optima(request):
    """
    Espera un JSON con:
    {
        "origen": "lat,lng",
        "destinos": ["lat1,lng1", "lat2,lng2", ...]
    }
    """
    origen = request.data.get('origen')
    destinos = request.data.get('destinos', [])
    ruta = calcular_ruta_optima(origen, destinos)
    
    return Response(ruta)