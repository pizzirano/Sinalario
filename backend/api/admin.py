from django.contrib import admin
from .models import Categoria, Dominio, Subcategoria, Termo, Video, Classificacao

# Registro de Dominio
@admin.register(Dominio)
class DominioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']  # 'id' é o campo padrão de chave primária
    search_fields = ['nome']  # Permite buscar por nome do domínio

# Registro de Termo
@admin.register(Termo)
class TermoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'dominio']  # Exibe id, nome e domínio relacionado
    list_filter = ['dominio']  # Filtra por domínio
    search_fields = ['nome', 'dominio__nome']  # Pesquisa por nome ou domínio relacionado

# Registro de Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'dominio']  # Exibe id, nome e domínio relacionado
    list_filter = ['dominio']  # Filtra por domínio
    search_fields = ['nome', 'dominio__nome']  # Pesquisa por nome ou domínio relacionado

# Registro de Subcategoria
@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'categoria']  # Exibe id, nome e categoria relacionada
    list_filter = ['categoria']  # Filtra por categoria
    search_fields = ['nome', 'categoria__nome']  # Pesquisa por nome ou categoria relacionada

# Registro de Vídeo
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'tipo_video', 'termo']  # Exibe id, título, tipo e termo relacionado
    list_filter = ['tipo_video', 'termo']  # Filtra por tipo e termo
    search_fields = ['titulo', 'termo__nome']  # Pesquisa por título ou termo relacionado

# Registro de Classificação
@admin.register(Classificacao)
class ClassificacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'termo', 'categoria']  # Exibe id, termo e categoria
    search_fields = ['termo_nome', 'categoria_nome']  # Pesquisa por nome de termo ou categoria