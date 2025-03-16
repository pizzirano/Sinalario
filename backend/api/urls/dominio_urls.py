from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.dominio_views import DominioViewSet

router = DefaultRouter()
router.register(r'dominios', DominioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]