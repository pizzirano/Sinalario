from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import Categoria
from api.serializers import CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]