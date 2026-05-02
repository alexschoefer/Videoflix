from django.db import models

# Create your models here.

class Video(models.Model):
    """
    Model representing a video in the application.
    Fields:
        title (CharField): The title of the video.
        description (TextField): A detailed description of the video content.
        created_at (DateTimeField): The timestamp when the video was created.
        category (CharField): The category or genre of the video.
        thumbnail_url (URLField): An optional URL pointing to the video's thumbnail image.
        CATEGORY_CHOICES (list): A predefined list of categories for the video.
    """

    CATEGORY_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Documentary', 'Documentary'),
        ('Animation', 'Animation'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    thumbnail_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        """
        String representation of the Video model, returning the title of the video.
        """
        return self.title