from rest_framework import generics
from rest_framework.permissions import AllowAny  # Adicionando a permissão AllowAny
from api.models import Video
from api.serializers import VideoSerializer

class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]  # Permite acesso sem autenticação

class VideoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]  # Permite acesso sem autenticação