from rest_framework import generics
from api.models import Subcategoria
from api.serializers import SubcategoriaSerializer
from rest_framework.permissions import AllowAny

class SubcategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer
    permission_classes = [AllowAny]

class SubcategoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer
    permission_classes = [AllowAny]