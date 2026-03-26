from allauth.account.models import EmailAddress


def email_dogrulandi_mi(user):
    """Kullanıcının en az bir doğrulanmış e-posta adresi var mı?"""
    return EmailAddress.objects.filter(user=user, verified=True).exists()


def dogrulama_maili_gonder(request, user):
    """Doğrulanmamış kullanıcıya doğrulama maili gönder (hata olursa sessizce geç)."""
    try:
        email_address = EmailAddress.objects.get(user=user, primary=True, verified=False)
        email_address.send_confirmation(request)
    except Exception:
        pass
