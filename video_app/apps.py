from django.apps import AppConfig


class VideoAppConfig(AppConfig):
    name = 'video_app'

    def ready(self):
        # Import signals to ensure they are registered when the app is ready
        print("VIDEO APP READY")
        import video_app.signals
