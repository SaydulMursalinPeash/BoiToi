from django.apps import AppConfig


class BoitoiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'boitoi'

    def ready(self):
        import boitoi.signals
