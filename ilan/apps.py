from django.apps import AppConfig


class IlanConfig(AppConfig):
    name = 'ilan'

    def ready(self):
        import ilan.signals
