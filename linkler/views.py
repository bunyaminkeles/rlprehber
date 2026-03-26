from django.shortcuts import get_object_or_404
from django.http import HttpResponsePermanentRedirect


def liste(request, eyalet_slug='rlp', stadt_slug=None):
    """Linkler sayfası yerler sayfasına taşındı — kalıcı yönlendirme."""
    if stadt_slug:
        return HttpResponsePermanentRedirect(f'/{eyalet_slug}/{stadt_slug}/yerler/')
    return HttpResponsePermanentRedirect(f'/{eyalet_slug}/yerler/')


def git(request, pk, eyalet_slug='rlp', stadt_slug=None):
    link = get_object_or_404(OnemliLink, pk=pk, aktif=True)
    return render(request, 'linkler/git.html', {'link': link})
