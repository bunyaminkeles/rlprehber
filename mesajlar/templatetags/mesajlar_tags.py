from django import template
from django.db.models import Q
from mesajlar.models import Konusma, Mesaj

register = template.Library()


@register.simple_tag
def okunmamis_sayi(user):
    if not user.is_authenticated:
        return 0
    return Mesaj.objects.filter(
        konusma__in=Konusma.objects.filter(Q(taraf1=user) | Q(taraf2=user)),
        okundu=False,
    ).exclude(gonderen=user).count()
