from rest_framework import status, viewsets
from authApp.models import Pregunta
from authApp.serializers import PreguntaSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class PreguntaView(viewsets.ModelViewSet):
    serializer_class = PreguntaSerializer
    
    def list(self, request):
        queryset = Pregunta.objects.all()
        serializer = PreguntaSerializer(queryset, many=True)
        return Response({'data': serializer.data})

    def retrieve(self, request, pk=None):
       pregunta = get_object_or_404(Pregunta, id=pk)
       serializer = PreguntaSerializer(pregunta)
       return Response({'data': serializer.data})

    def update(self, request, pk=None):
        pregunta = pregunta.objects.get(id=pk)
        serializer = PreguntaSerializer(pregunta, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = PreguntaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        pregunta = get_object_or_404(Pregunta, id=pk)
        pregunta.delete()
        return Response({'status': 'success'})