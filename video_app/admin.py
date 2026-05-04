from django.contrib import admin
from video_app.models import Video

# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    """
    Admin interface for the Video model.
    This class defines the configuration for how the Video model is displayed and managed in the Django admin interface.
     Attributes:
        list_display (tuple): A tuple of field names to be displayed in the list view of the admin interface.
        search_fields (tuple): A tuple of field names that can be searched using the search box in the admin interface.
        ordering (tuple): A tuple defining the default ordering of the video records in the admin interface, in this case, ordered by creation date in descending order.
    """
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
