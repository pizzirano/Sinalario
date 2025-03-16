from django.db import models

# Modelo de Domínio
class Dominio(models.Model):
    nome = models.CharField(max_length=30, unique=True)

    def _str_(self):
        return self.nome

# Modelo de Termo
class Termo(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    descricao = models.TextField(blank=True, null=True)
    dominio = models.ForeignKey(Dominio, on_delete=models.CASCADE, related_name="termos")

    def _str_(self):
        return self.nome

# Modelo de Categoria
class Categoria(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    dominio = models.ForeignKey(Dominio, on_delete=models.CASCADE, related_name="categorias")

    def _str_(self):
        return self.nome

# Modelo de Subcategoria
class Subcategoria(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="subcategorias")

    def _str_(self):
        return self.nome

class Video(models.Model):
    TIPOS_VIDEO = [
        ('Sinal', 'Sinal'),
        ('Soletrando', 'Termo em Libras Soletrando'),
        ('Significado', 'Significado'),
    ]

    titulo = models.CharField(max_length=30)
    video = models.FileField(upload_to='videos/')  # Salva em media/videos/
    tipo_video = models.CharField(max_length=20, choices=TIPOS_VIDEO)
    termo = models.ForeignKey('Termo', on_delete=models.CASCADE, related_name="videos")

    def _str_(self):
        return self.titulo

# Modelo de Classificação
class Classificacao(models.Model):
    termo = models.ForeignKey(Termo, on_delete=models.CASCADE, related_name="classificacoes")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="classificacoes")

    class Meta:
        unique_together = ('termo', 'categoria')

    def _str_(self):
        return f"{self.termo.nome} - {self.categoria.nome}"