from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Endpoints da API
    path('api/auth/', include('api.urls.auth_urls')),
    path('api/termo/', include('api.urls.termo_urls')),
    path('api/dominio/', include('api.urls.dominio_urls')),
    path('api/categoria/', include('api.urls.categoria_urls')),
    path('api/subcategoria/', include('api.urls.subcategoria_urls')),
    path('api/video/', include('api.urls.video_urls')),

    # Endpoints para JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Configuração para arquivos estáticos e de mídia
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)