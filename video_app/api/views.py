import os
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import VideoSerializer
from video_app.models import Video
from auth_app.api.authentication import CustomJWTAuthentication
from django.http import HttpResponse

class VideoListView(generics.ListAPIView):
    """
    APIView to handle GET requests for retrieving a list of videos.
    This view is protected by JWT authentication and requires the user to be authenticated.
    
    Attributes:
        authentication_classes (list): A list of authentication classes to be used for this view.
        permission_classes (list): A list of permission classes to be applied to this view.
        serializer_class (Serializer): The serializer class used to serialize the video data.
    """
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = VideoSerializer
    queryset = Video.objects.all().order_by('-created_at')
      
class HLSManifestView(APIView):
    """
    APIView to handle GET requests for retrieving the HLS master playlist for a specific video.
    This view is protected by JWT authentication and requires the user to be authenticated.
    
    Attributes:
        authentication_classes (list): A list of authentication classes to be used for this view.
        permission_classes (list): A list of permission classes to be applied to this view.
    """
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, movie_id, resolution):
        """
        Handles GET requests to retrieve the HLS master playlist for a specific video based on the provided movie_id and resolution.
        Args:
            request (Request): The HTTP request object.
            movie_id (int): The ID of the video for which to retrieve the HLS master playlist.
            resolution (str): The resolution of the HLS stream to retrieve (e.g., "480p", "720p", "1080p").
        Returns:
            Response: An HTTP response containing the content of the HLS master playlist if found, or an error message if the video or manifest is not found.
        """
        try:
            video = Video.objects.get(id=movie_id)

            hls_path = os.path.join(
                settings.MEDIA_ROOT,
                "hls",
                str(movie_id),
                resolution,
                "index.m3u8"
            )

            if not os.path.exists(hls_path):
                return Response(
                    {"error": "Manifest not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            with open(hls_path, "r") as file:
                content = file.read()

            return HttpResponse(
                content,
                content_type="application/vnd.apple.mpegurl"
            )

        except Video.DoesNotExist:
            return Response(
                {"error": "Video not found"},
                status=status.HTTP_404_NOT_FOUND
            )