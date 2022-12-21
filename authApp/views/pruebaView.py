from rest_framework import status, viewsets
from authApp.models import Prueba
from authApp.serializers import PruebaSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class PruebaView(viewsets.ModelViewSet):
    serializer_class = PruebaSerializer
    
    def list(self, request):
        queryset = Prueba.objects.all()
        serializer = PruebaSerializer(queryset, many=True)
        return Response({'data': serializer.data})

    def retrieve(self, request, pk=None):
       prueba = get_object_or_404(Prueba, id=pk)
       serializer = PruebaSerializer(prueba)
       return Response({'data': serializer.data})

    def update(self, request, pk=None):
        prueba = prueba .objects.get(id=pk)
        serializer = PruebaSerializer(prueba, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = PruebaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        prueba = get_object_or_404(Prueba, id=pk)
        prueba.delete()
        return Response({'status': 'success'})