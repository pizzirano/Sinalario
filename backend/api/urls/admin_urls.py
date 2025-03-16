from django.urls import path
from api.views.admin_views import AdminDashboardView, UserListView, UserDetailView

urlpatterns = [
    path('dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('usuarios/', UserListView.as_view(), name='user-list'),
    path('usuarios/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]