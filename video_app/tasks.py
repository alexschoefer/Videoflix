# standard library imports
import os
import subprocess

# third-party imports
from django.conf import settings

# local imports
from video_app.models import Video

def convert_video_to_hls(movie_id):
    """
    Task to convert a video to HLS format and create a thumbnail.
    Args:        
        movie_id (int): The ID of the video to be processed.
    This function retrieves the video instance using the provided movie_id, converts the video to HLS format with multiple resolutions, and creates a thumbnail for the video. 
    The converted HLS files are stored in a structured directory under MEDIA_ROOT, and the thumbnail is saved as a JPEG image. 
    The thumbnail URL is then updated in the Video model instance.
    """
    video = Video.objects.get(id=movie_id)
    target = video.video_file.path
    _convert_video_to_hls_resolutions_format(movie_id, target)
    _create_video_thumbnail(movie_id, target, video)

def _convert_video_to_hls_resolutions_format(movie_id, target):
    """
    Helper function to convert a video to HLS format with multiple resolutions.
    Args:
        movie_id (int): The ID of the video being processed.
        target (str): The file path of the original video to be converted.
    This function defines a set of resolutions (480p, 720p, 1080p) and uses FFmpeg to convert the original video into HLS format for each resolution.
    The converted HLS files are stored in a structured directory under MEDIA_ROOT, organized by video ID and resolution.    
    """
    resolutions = {
        "480p": "854:480",
        "720p": "1280:720",
        "1080p": "1920:1080",
    }

    for resolution, size in resolutions.items():
        output_dir = os.path.join(settings.MEDIA_ROOT, f'hls/{movie_id}/{resolution}')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'index.m3u8')

        command = [
            'ffmpeg','-i', target,
            '-vf', f'scale={size}',
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-start_number', '0',
            '-hls_time', '10',
            '-hls_list_size', '0',
            '-hls_segment_filename', os.path.join(output_dir, '%03d.ts'),
            '-f', 'hls',
            output_path
        ]

        subprocess.run(command, check=True)

def _create_video_thumbnail(movie_id, target, video):
    """
    Helper function to create a thumbnail for a video.
    Args:
        movie_id (int): The ID of the video being processed.
        target (str): The file path of the original video from which to create the thumbnail.
        video (Video): The Video model instance for which the thumbnail is being created.
    This function uses FFmpeg to extract a frame from the original video (at the 10-second mark) and saves it as a JPEG image in a structured directory under MEDIA_ROOT.
    The thumbnail URL is then updated in the Video model instance and saved to the database.
    """
    thumbnail_filename = f"{movie_id}.jpg"
    thumbnail_path = os.path.join(settings.MEDIA_ROOT, "thumbnails", thumbnail_filename)
    os.makedirs(os.path.dirname(thumbnail_path), exist_ok=True)

    command = [
    'ffmpeg',
    '-y',
    '-i', target,
    '-ss', '00:00:10',
    '-frames:v', '1',
    '-q:v', '2',
    '-update', '1',
    thumbnail_path
]

    subprocess.run(command, check=True)
    video.thumbnail_url.name = f"thumbnails/{thumbnail_filename}"
    video.save(update_fields=["thumbnail_url"])
