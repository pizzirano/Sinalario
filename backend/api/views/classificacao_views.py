from rest_framework import viewsets
from rest_framework.permissions import AllowAny  # Altere para AllowAny
from api.models import Classificacao
from api.serializers import ClassificacaoSerializer

class ClassificacaoViewSet(viewsets.ModelViewSet):
    queryset = Classificacao.objects.all()
    serializer_class = ClassificacaoSerializer
    permission_classes = [AllowAny]  # Permite acesso sem autenticação