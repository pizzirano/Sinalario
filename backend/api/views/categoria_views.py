from rest_framework import viewsets
from api.models import Categoria
from api.serializers import CategoriaSerializer
from rest_framework.permissions import AllowAny

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]  # Permite o acesso a qualquer pessoa sem autenticação