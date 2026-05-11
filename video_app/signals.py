# standard Library
import os

# third-party
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

# local Imports
from .models import Video
from .tasks import convert_video_to_hls

"""
Signal handler for the post_save signal of the Video model.
"""
@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    """
    Signal handler for the post_save signal of the Video model. 
    This function is triggered whenever a Video instance is saved. 
    If the instance is newly created, it enqueues a task to convert the video to HLS format and create a thumbnail using Django RQ.
    Args:
        sender (Model): The model class that sent the signal.
        instance (Video): The instance of the Video model that was saved.
        created (bool): A boolean indicating whether the instance was created (True) or updated (False).
        **kwargs: Additional keyword arguments passed by the signal.
    """
    if created:
        import django_rq
        queue = django_rq.get_queue('default')
        queue.enqueue(convert_video_to_hls, instance.id)

"""
Signal handler for the post_delete signal of the Video model.
"""
@receiver(post_delete, sender=Video)
def video_post_delete(sender, instance, **kwargs):
    """
    Signal handler for the post_delete signal of the Video model.
    This function is triggered whenever a Video instance is deleted.
    It checks if the video file and thumbnail associated with the deleted instance exist on the filesystem, and if they do, it removes them to free up storage space.
    Args:
    sender (Model): The model class that sent the signal.
    instance (Video): The instance of the Video model that was deleted.
    **kwargs: Additional keyword arguments passed by the signal.
    """
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)
    if instance.thumbnail_url:
        if os.path.isfile(instance.thumbnail_url.path):
            os.remove(instance.thumbnail_url.path)