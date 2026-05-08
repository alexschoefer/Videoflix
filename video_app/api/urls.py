from django.urls import path
from .views import VideoListView, HLSManifestView, HLSSegmentView

urlpatterns = [
    path('api/video/', VideoListView.as_view(), name='video-list'),
    path('api/video/<int:movie_id>/<str:resolution>/index.m3u8', HLSManifestView.as_view(), name='hls-master-playlist'),
    path('api/video/<int:movie_id>/<str:resolution>/<str:segment>', HLSSegmentView.as_view(), name='hls-segment'),
]
