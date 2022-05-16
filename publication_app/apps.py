from django.apps import AppConfig


class PublicationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'publication_app'

    def ready(self):
        from .signals import user