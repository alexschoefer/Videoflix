from django.apps import AppConfig


class VideoAppConfig(AppConfig):
    name = 'video_app'

    def ready(self):
        # Import signals to ensure they are registered when the app is ready
        import video_app.signals
