import os
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import VideoSerializer
from video_app.models import Video
from rest_framework_simplejwt.authentication import JWTAuthentication

class VideoListView(generics.ListAPIView):
    """
    APIView to handle GET requests for retrieving a list of videos.
    This view is protected by JWT authentication and requires the user to be authenticated.
    
    Attributes:
        authentication_classes (list): A list of authentication classes to be used for this view.
        permission_classes (list): A list of permission classes to be applied to this view.
        serializer_class (Serializer): The serializer class used to serialize the video data.
    """
    authentication_classes = [JWTAuthentication]
    serializer_class = VideoSerializer
    queryset = Video.objects.all().order_by('-created_at')
      
