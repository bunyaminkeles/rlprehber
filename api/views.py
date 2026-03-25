import subprocess, sys
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.conf import settings
from django.core.management import call_command


def health(request):
    """Basit health check — cron-job.org veya uptime monitörler için."""
    return JsonResponse({
        'status': 'ok',
        'timestamp': timezone.now().isoformat(),
        'service': 'rlp-rehber',
    })


def _token_kontrol(request):
    secret = getattr(settings, 'CRON_SECRET', None)
    if not secret:
        return None, JsonResponse({'error': 'CRON_SECRET ayarlanmamış.'}, status=500)
    token = (
        request.GET.get('token')
        or request.POST.get('token')
        or request.headers.get('Authorization', '').removeprefix('Bearer ').strip()
    )
    if token != secret:
        return None, JsonResponse({'error': 'Yetkisiz.'}, status=401)
    return secret, None


@csrf_exempt
def rss_cek(request):
    """RSS beslemelerini çeker. ?token=<CRON_SECRET> gerekli."""
    _, hata = _token_kontrol(request)
    if hata:
        return hata
    try:
        from io import StringIO
        out = StringIO()
        call_command('rss_cek', stdout=out, stderr=out)
        return JsonResponse({
            'status': 'ok',
            'timestamp': timezone.now().isoformat(),
            'output': out.getvalue(),
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'detail': str(e)}, status=500)


@csrf_exempt
def cleanup_s3(request):
    """
    Forum klasöründeki 15 günden eski ve DB'de referansı olmayan S3 dosyalarını siler.
    ?token=<CRON_SECRET> gerekli.
    """
    _, hata = _token_kontrol(request)
    if hata:
        return hata

    if not getattr(settings, 'AWS_STORAGE_BUCKET_NAME', None):
        return JsonResponse({'error': 'S3 yapılandırılmamış.'}, status=500)

    try:
        import boto3
        from datetime import timedelta
        from forum.models import Konu, Yorum

        sinir = timezone.now() - timedelta(days=15)

        s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME,
        )

        # DB'deki tüm aktif resim yollarını topla
        aktif = set()
        for r in Konu.objects.exclude(resim='').exclude(resim=None).values_list('resim', flat=True):
            aktif.add(str(r))
        for r in Yorum.objects.exclude(resim='').exclude(resim=None).values_list('resim', flat=True):
            aktif.add(str(r))

        silinen = []
        paginator = s3.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Prefix='forum/'):
            for obj in page.get('Contents', []):
                key = obj['Key']
                last_modified = obj['LastModified'].replace(tzinfo=timezone.utc)
                if last_modified < sinir and key not in aktif:
                    s3.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=key)
                    silinen.append(key)

        return JsonResponse({
            'status': 'ok',
            'timestamp': timezone.now().isoformat(),
            'silinen_sayi': len(silinen),
            'silinenler': silinen,
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'detail': str(e)}, status=500)


@csrf_exempt
def seed_calistir(request):
    """
    Seed scriptlerini çalıştırır. ?token=<CRON_SECRET> gerekli.
    ?script=takvim|linkler|yerler|blog|hepsi (varsayılan: hepsi)
    """
    _, hata = _token_kontrol(request)
    if hata:
        return hata

    script_param = request.GET.get('script', 'hepsi')
    scriptler = {
        'takvim': 'takvim_seed.py',
        'linkler': 'linkler_seed.py',
        'yerler':  'yerler_seed.py',
        'blog':    'blog_yazilari_ekle.py',
        'forum':   'forum_seed.py',
    }

    if script_param == 'hepsi':
        calistirilacak = list(scriptler.values())
    elif script_param in scriptler:
        calistirilacak = [scriptler[script_param]]
    else:
        return JsonResponse({'error': f'Geçersiz script: {script_param}'}, status=400)

    ciktilar = {}
    for script in calistirilacak:
        try:
            sonuc = subprocess.run(
                [sys.executable, script],
                capture_output=True, text=True, timeout=60
            )
            ciktilar[script] = sonuc.stdout + sonuc.stderr
        except Exception as e:
            ciktilar[script] = str(e)

    return JsonResponse({
        'status': 'ok',
        'timestamp': timezone.now().isoformat(),
        'ciktilar': ciktilar,
    })
