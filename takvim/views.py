from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.utils import timezone
from .models import Etkinlik


def liste(request, stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    if stadt:
        etkinlikler = Etkinlik.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
            tarih__gte=timezone.now().date()
        )
    else:
        etkinlikler = Etkinlik.objects.filter(
            scope='eyalet',
            tarih__gte=timezone.now().date()
        )

    return render(request, 'takvim/liste.html', {
        'etkinlikler': etkinlikler,
        'stadt': stadt,
    })


# alias
takvim = liste
