from django.shortcuts import render
from Api.imagen.serializer import ImagenProductoColorSerializer
from Api.imagen.models import ImagenProductoColor
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class ImagenProductoColorViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las imágenes de productos por color.
    Permite operaciones CRUD y una búsqueda personalizada por producto y color.
    """
    # permission_classes = [IsAuthenticated]  # Descomenta si quieres requerir autenticación

    # Consulta todos los objetos de ImagenProductoColor
    queryset = ImagenProductoColor.objects.all()
    # Usa el serializer correspondiente para este modelo
    serializer_class = ImagenProductoColorSerializer

    @action(detail=False, methods=['get'])
    def buscar(self, request):
        """
        Endpoint personalizado para buscar una imagen por id de producto y color.
        Ejemplo de uso:
        GET /api/v1/imagen-producto-color/buscar/?producto_id=1&color_id=2
        """
        # Obtiene los parámetros de la URL
        producto_id = request.query_params.get('producto_id')
        color_id = request.query_params.get('color_id')

        # Valida que ambos parámetros estén presentes
        if not producto_id or not color_id:
            return Response({'error': 'Faltan parámetros'}, status=status.HTTP_400_BAD_REQUEST)

        # Busca la primera imagen que coincida con el producto y color
        imagen = ImagenProductoColor.objects.filter(producto_id=producto_id, color_id=color_id).first()

        # Si encuentra una imagen, la serializa y la retorna
        if imagen:
            serializer = self.get_serializer(imagen)
            return Response(serializer.data)
        else:
            # Si no encuentra, retorna un error 404
            return Response({'error': 'No encontrada'}, status=status.HTTP_404_NOT_FOUND)

# Ahora puedes buscar así:
# GET /api/v1/imagen-producto-color/buscar/?producto_id=1&color_id=2