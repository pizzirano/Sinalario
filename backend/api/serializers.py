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

class SubcategoriaSerializer(serializers.ModelSerializer):
    categoria = serializers.SlugRelatedField(
        queryset=Categoria.objects.all(), slug_field='nome'
    )  # Usa o nome da categoria em vez do ID

    class Meta:
        model = Subcategoria
        fields = ['id', 'nome', 'categoria']

# Vídeo
class VideoSerializer(serializers.ModelSerializer):
    video = serializers.FileField(required=True)
    termo = serializers.CharField(write_only=True)  # Recebe o nome do termo
    descricao = serializers.CharField(write_only=True)  # Recebe a descrição do termo
    dominio = serializers.IntegerField(write_only=True)  # Recebe o ID do domínio

    class Meta:
        model = Video
        fields = ['video', 'termo', 'descricao', 'dominio']

    def create(self, validated_data):
        termo_nome = validated_data.pop('termo')  # Pega o nome do termo
        descricao = validated_data.pop('descricao')  # Pega a descrição
        dominio_id = validated_data.pop('dominio')  # Pega o ID do domínio

        # Verifica se o termo existe, se não cria
        termo, created = Termo.objects.get_or_create(
            nome=termo_nome,
            descricao=descricao,  # Passa a descrição ao criar o termo
            dominio_id=dominio_id  # Associa o domínio ao termo
        )

        # Cria o vídeo e associa ao termo
        video = Video.objects.create(termo=termo, **validated_data)
        return video

#  Classificacao
class ClassificacaoSerializer(serializers.ModelSerializer):
    termo = TermoSerializer()  # Incluindo o termo da classificação
    categoria = CategoriaSerializer()  # Incluindo a categoria da classificação

    class Meta:
        model = Classificacao
        fields = ['id', 'termo', 'categoria']