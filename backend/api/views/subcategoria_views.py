from rest_framework import generics
from api.models import Subcategoria
from api.serializers import SubcategoriaSerializer

# View para listar e criar subcategorias
class SubcategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer

# View para recuperar, atualizar ou destruir subcategorias
class SubcategoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer