from django.apps import AppConfig


class UserSignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_signals'

    def ready(self):
        import user_signals.signals