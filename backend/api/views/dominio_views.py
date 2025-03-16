from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import Dominio
from api.serializers import DominioSerializer

class DominioViewSet(viewsets.ModelViewSet):
    queryset = Dominio.objects.all()
    serializer_class = DominioSerializer
    permission_classes = [IsAuthenticated]