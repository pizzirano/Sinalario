from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.categoria_views import CategoriaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]