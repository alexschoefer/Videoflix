from django.urls import path
from .views import VideoListView

urlpatterns = [
    path('api/video/', VideoListView.as_view(), name='video-list'),
]
