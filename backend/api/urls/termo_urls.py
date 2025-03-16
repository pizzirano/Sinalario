from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.termo_views import TermoViewSet

router = DefaultRouter()
router.register(r'termos', TermoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]