from django.contrib import admin
from django.utils.html import format_html
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    readonly_fields = ("thumbnail_preview",)

    fieldsets = (
        (
            "Video Information",
            {
                "fields": (
                    "title",
                    "description",
                    "category",
                    "video_file",
                )
            },
        ),
        (
            "Generated Media",
            {
                "description": (
                    "Thumbnail is generated automatically "
                    "after video processing."
                ),
                "fields": ("thumbnail_preview",),
            },
        ),
    )

    def thumbnail_preview(self, obj):
        """
        Safely display generated thumbnail preview.
        """
        if obj.thumbnail_url and hasattr(obj.thumbnail_url, "url"):
            return format_html(
                '<img src="{}" width="200" style="border-radius:8px;" />',
                obj.thumbnail_url.url
            )

        return "Thumbnail will be generated after processing."

    thumbnail_preview.short_description = "Thumbnail Preview"