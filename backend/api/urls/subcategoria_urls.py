from django.urls import path
from api.views.subcategoria_views import SubcategoriaListCreateView, SubcategoriaRetrieveUpdateDestroyView

urlpatterns = [
    path('', SubcategoriaListCreateView.as_view(), name='subcategoria-list-create'),
    path('<int:pk>/', SubcategoriaRetrieveUpdateDestroyView.as_view(), name='subcategoria-detail'),
]