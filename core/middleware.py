from django.http import HttpResponseRedirect

from .models import SiteZiyaret

SESSION_KEY = '_site_ziyaret_sayildi'

_HONEYPOT_FIELD = 'website'
_GUARDED_PATHS = {'/accounts/login/', '/accounts/signup/'}


class HoneypotMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.method == 'POST'
            and request.path in _GUARDED_PATHS
            and request.POST.get(_HONEYPOT_FIELD)
        ):
            return HttpResponseRedirect(request.path)
        return self.get_response(request)


class ZiyaretSayaciMiddleware:
    """Her benzersiz oturumu bir kez sayar."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.get(SESSION_KEY):
            try:
                SiteZiyaret.artir()
                request.session[SESSION_KEY] = True
            except Exception:
                pass
        return self.get_response(request)
