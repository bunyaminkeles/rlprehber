from .models import Stadt


def alle_staedte(request):
    """Tüm aktif şehirleri her template'e sağlar (navbar dropdown için)."""
    return {
        'alle_staedte': Stadt.objects.filter(aktiv=True),
    }
