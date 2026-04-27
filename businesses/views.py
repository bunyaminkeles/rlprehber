import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import F
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import LocalBusiness, BusinessAnalytics, BusinessCategory
from stadt.models import Stadt


def business_list(request):
    today = timezone.localdate()
    aktif_isletmeler = (
        LocalBusiness.objects
        .filter(is_published=True, end_date__gte=today)
        .select_related('city', 'category', 'subscription_plan')
        .order_by('category__name', 'name')
    )

    # Kategorilere göre grupla
    kategoriler = []
    seen = {}
    for isletme in aktif_isletmeler:
        cat = isletme.category
        cat_id = cat.id if cat else 0
        if cat_id not in seen:
            seen[cat_id] = {'kategori': cat, 'isletmeler': []}
            kategoriler.append(seen[cat_id])
        seen[cat_id]['isletmeler'].append(isletme)

    return render(request, 'businesses/business_list.html', {
        'kategoriler': kategoriler,
        'toplam': aktif_isletmeler.count(),
    })


@require_POST
def track_business_click(request, slug):
    business = get_object_or_404(LocalBusiness, slug=slug, is_published=True)

    try:
        payload = json.loads(request.body)
        action = payload.get('action', '')
    except (json.JSONDecodeError, ValueError):
        return JsonResponse({'status': 'error', 'message': 'Geçersiz JSON'}, status=400)

    if action not in ('view', 'whatsapp'):
        return JsonResponse({'status': 'error', 'message': 'Geçersiz action'}, status=400)

    record, _ = BusinessAnalytics.objects.get_or_create(
        business=business,
        date=timezone.localdate(),
    )

    if action == 'view':
        BusinessAnalytics.objects.filter(pk=record.pk).update(views=F('views') + 1)
    else:
        BusinessAnalytics.objects.filter(pk=record.pk).update(whatsapp_clicks=F('whatsapp_clicks') + 1)

    return JsonResponse({'status': 'ok'})


def category_list(request, kategori_slug):
    kategori = get_object_or_404(BusinessCategory, slug=kategori_slug)
    today = timezone.localdate()

    isletmeler = list(
        LocalBusiness.objects
        .filter(category=kategori, is_published=True, end_date__gte=today)
        .select_related('city', 'category', 'subscription_plan')
        .order_by('name')
    )

    tum_kategoriler = BusinessCategory.objects.all().order_by('name')

    # Schema.org — ItemList + LocalBusiness
    liste_elemanlari = []
    for idx, isletme in enumerate(isletmeler, 1):
        item = {
            "@type": "ListItem",
            "position": idx,
            "item": {
                "@type": "LocalBusiness",
                "name": isletme.name,
            },
        }
        if isletme.description or isletme.slogan:
            item["item"]["description"] = isletme.description or isletme.slogan
        if isletme.city:
            item["item"]["address"] = {
                "@type": "PostalAddress",
                "addressLocality": isletme.city.name,
                "addressCountry": "DE",
            }
        if isletme.whatsapp_number:
            item["item"]["telephone"] = isletme.whatsapp_number
        if isletme.website_url:
            item["item"]["url"] = isletme.website_url
        liste_elemanlari.append(item)

    schema = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": f"{kategori.name} — Lokal Uzmanlar",
        "description": f"Almanya'da Türkçe hizmet veren {kategori.name.lower()} uzmanları",
        "numberOfItems": len(liste_elemanlari),
        "itemListElement": liste_elemanlari,
    }

    return render(request, 'businesses/category_list.html', {
        'kategori': kategori,
        'isletmeler': isletmeler,
        'tum_kategoriler': tum_kategoriler,
        'schema_json': json.dumps(schema, ensure_ascii=False),
    })


def stadt_business_list(request, eyalet_slug, stadt_slug):
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True)
    today = timezone.localdate()

    aktif_isletmeler = (
        LocalBusiness.objects
        .filter(city=stadt, is_published=True, end_date__gte=today)
        .select_related('city', 'category', 'subscription_plan')
        .order_by('category__name', 'name')
    )

    kategoriler = []
    seen = {}
    for isletme in aktif_isletmeler:
        cat = isletme.category
        cat_id = cat.id if cat else 0
        if cat_id not in seen:
            seen[cat_id] = {'kategori': cat, 'isletmeler': []}
            kategoriler.append(seen[cat_id])
        seen[cat_id]['isletmeler'].append(isletme)

    return render(request, 'businesses/business_list.html', {
        'kategoriler': kategoriler,
        'toplam': aktif_isletmeler.count(),
        'stadt': stadt,
        'eyalet_slug': eyalet_slug,
    })


def stadt_category_list(request, eyalet_slug, stadt_slug, kategori_slug):
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True)
    kategori = get_object_or_404(BusinessCategory, slug=kategori_slug)
    today = timezone.localdate()

    isletmeler = list(
        LocalBusiness.objects
        .filter(city=stadt, category=kategori, is_published=True, end_date__gte=today)
        .select_related('city', 'category', 'subscription_plan')
        .order_by('name')
    )

    tum_kategoriler = BusinessCategory.objects.filter(
        businesses__city=stadt,
        businesses__is_published=True,
        businesses__end_date__gte=today,
    ).distinct().order_by('name')

    liste_elemanlari = []
    for idx, isletme in enumerate(isletmeler, 1):
        item = {
            "@type": "ListItem",
            "position": idx,
            "item": {
                "@type": "LocalBusiness",
                "name": isletme.name,
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": stadt.name,
                    "addressCountry": "DE",
                },
            },
        }
        if isletme.description or isletme.slogan:
            item["item"]["description"] = isletme.description or isletme.slogan
        if isletme.whatsapp_number:
            item["item"]["telephone"] = isletme.whatsapp_number
        if isletme.website_url:
            item["item"]["url"] = isletme.website_url
        liste_elemanlari.append(item)

    schema = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": f"{stadt.name} {kategori.name} — Lokal Uzmanlar",
        "description": f"{stadt.name}'da Türkçe hizmet veren {kategori.name.lower()} uzmanları",
        "numberOfItems": len(liste_elemanlari),
        "itemListElement": liste_elemanlari,
    }

    return render(request, 'businesses/category_list.html', {
        'kategori': kategori,
        'isletmeler': isletmeler,
        'tum_kategoriler': tum_kategoriler,
        'stadt': stadt,
        'eyalet_slug': eyalet_slug,
        'schema_json': json.dumps(schema, ensure_ascii=False),
    })
