from allauth.account.models import EmailAddress


def email_dogrulandi_mi(user):
    """Kullanıcının en az bir doğrulanmış e-posta adresi var mı?"""
    return EmailAddress.objects.filter(user=user, verified=True).exists()
