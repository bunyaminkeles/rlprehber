from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class DuyurularConfig(AppConfig):
    name = 'duyurular'

    def ready(self):
        logger.warning("🚀 [APP READY] Duyurular uygulaması başlatıldı ve sinyaller yükleniyor.")
        import duyurular.signals
