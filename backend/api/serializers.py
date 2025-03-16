from rest_framework import serializers
from .models import Dominio, Termo, Categoria, Subcategoria, Video, Classificacao

#  Dominio
class DominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dominio
        fields = ['id', 'nome']

# Termo
class TermoSerializer(serializers.ModelSerializer):
    dominio = serializers.PrimaryKeyRelatedField(queryset=Dominio.objects.all())  # Aceita apenas o ID

    class Meta:
        model = Termo
        fields = ['id', 'nome', 'descricao', 'dominio']

#  Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    dominio = DominioSerializer()  # Incluindo o domínio da categoria

    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'dominio']

#  Subcategoria
class SubcategoriaSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()  # Incluindo a categoria da subcategoria

    class Meta:
        model = Subcategoria
        fields = ['id', 'nome', 'categoria']

# Vídeo
class VideoSerializer(serializers.ModelSerializer):
    termo = serializers.PrimaryKeyRelatedField(queryset=Termo.objects.all())  # Apenas ID

    class Meta:
        model = Video
        fields = ['id', 'titulo', 'video', 'tipo_video', 'termo']

#  Classificacao
class ClassificacaoSerializer(serializers.ModelSerializer):
    termo = TermoSerializer()  # Incluindo o termo da classificação
    categoria = CategoriaSerializer()  # Incluindo a categoria da classificação

    class Meta:
        model = Classificacao
        fields = ['id', 'termo', 'categoria']