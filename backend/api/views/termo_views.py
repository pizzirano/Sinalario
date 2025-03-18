from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import Termo
from api.serializers import TermoSerializer

class TermoViewSet(viewsets.ModelViewSet):
    queryset = Termo.objects.all()
    serializer_class = TermoSerializer
    #permission_classes = [IsAuthenticated]