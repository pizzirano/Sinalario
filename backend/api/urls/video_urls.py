from django.urls import path
from api.views.video_views import VideoListCreateView, VideoRetrieveUpdateDestroyView

urlpatterns = [
    path('', VideoListCreateView.as_view(), name='video-list-create'),
    path('<int:pk>/', VideoRetrieveUpdateDestroyView.as_view(), name='video-detail'),
]