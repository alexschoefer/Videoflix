from video_app.models import Video
from rest_framework import serializers

class VideoSerializer(serializers.ModelSerializer):
    """
    Serializer for the Video model, converting Video instances to JSON format and vice versa.
    """
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ['id','created_at', 'title', 'description', 'thumbnail_url' , 'category']

    def get_thumbnail_url(self, obj):
        """
        Method to retrieve the absolute URL of the video's thumbnail image.
        Args:
            obj (Video): The Video instance for which to retrieve the thumbnail URL.
        Returns:
            str: The absolute URL of the thumbnail image if available, otherwise None.
        """
        request = self.context.get('request')
        if obj.thumbnail_url and request:
            return request.build_absolute_uri(obj.thumbnail_url)
        return None