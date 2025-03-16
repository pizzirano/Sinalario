from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import Classificacao
from api.serializers import ClassificacaoSerializer

class ClassificacaoViewSet(viewsets.ModelViewSet):
    queryset = Classificacao.objects.all()
    serializer_class = ClassificacaoSerializer
    permission_classes = [IsAuthenticated] 