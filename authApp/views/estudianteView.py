from rest_framework import status, viewsets
from authApp.models import Estudiante
from authApp.serializers import EstudianteSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class EstudianteView(viewsets.ModelViewSet):
    serializer_class = EstudianteSerializer
    
    def list(self, request):
        queryset = Estudiante.objects.all()
        serializer = EstudianteSerializer(queryset, many=True)
        return Response({'data': serializer.data})

    def retrieve(self, request, pk=None):
       estudiante = get_object_or_404(Estudiante, id=pk)
       serializer = EstudianteSerializer(estudiante)
       return Response({'data': serializer.data})

    def update(self, request, pk=None):
        estudiante = Estudiante.objects.get(id=pk)
        serializer = EstudianteSerializer(estudiante, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = EstudianteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        estudiante = get_object_or_404(Estudiante, id=pk)
        estudiante.delete()
        return Response({'status': 'success'})