from django.apps import AppConfig


class DuyurularConfig(AppConfig):
    name = 'duyurular'

    def ready(self):
        import duyurular.signals
