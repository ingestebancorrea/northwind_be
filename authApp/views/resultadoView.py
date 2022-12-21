from rest_framework import status, viewsets
from authApp.models import Resultado
from authApp.serializers import ResultadoSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ResultadoView(viewsets.ModelViewSet):
    serializer_class = ResultadoSerializer
    
    def list(self, request):
        queryset = Resultado.objects.all()
        serializer = ResultadoSerializer(queryset, many=True)
        return Response({'data': serializer.data})

    def retrieve(self, request, pk=None):
        resultado = get_object_or_404(resultado, id=pk)
        serializer = ResultadoSerializer(resultado)
        return Response({'data': serializer.data})

    def update(self, request, pk=None):
        resultado = resultado.objects.get(id=pk)
        serializer = ResultadoSerializer(resultado, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = ResultadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        resultado = get_object_or_404(Resultado, id=pk)
        resultado.delete()
        return Response({'status': 'success'})