"""
Data migration: Rheinland-Pfalz kreisfreie Städte ekle.
"""
from django.db import migrations

RLP_STAEDTE = [
    {
        'name': 'Koblenz',
        'slug': 'koblenz',
        'typ': 'kreisfrei',
        'lat': 50.3569,
        'lng': 7.5890,
        'population': 114000,
        'auslaenderbehorde_url': 'https://www.koblenz.de/leben-in-koblenz/buergerservice/auslaenderbehoerde/',
        'termin_url': '',
        'beschreibung': 'Ren ve Mosel nehirlerinin kavşağında tarihi bir şehir.',
    },
    {
        'name': 'Trier',
        'slug': 'trier',
        'typ': 'kreisfrei',
        'lat': 49.7490,
        'lng': 6.6371,
        'population': 111000,
        'auslaenderbehorde_url': 'https://www.trier.de/rathaus-buerger-in/auslaenderbehoerde/',
        'termin_url': '',
        'beschreibung': "Almanya'nın en eski şehirlerinden biri, Roma mirası ile ünlü.",
    },
    {
        'name': 'Kaiserslautern',
        'slug': 'kaiserslautern',
        'typ': 'kreisfrei',
        'lat': 49.4440,
        'lng': 7.7689,
        'population': 99000,
        'auslaenderbehorde_url': 'https://www.kaiserslautern.de/buergerservice/auslaenderbehoerde/',
        'termin_url': '',
        'beschreibung': 'Pfälzerwald eteklerinde sanayi ve üniversite şehri.',
    },
    {
        'name': 'Ludwigshafen am Rhein',
        'slug': 'ludwigshafen',
        'typ': 'kreisfrei',
        'lat': 49.4774,
        'lng': 8.4452,
        'population': 172000,
        'auslaenderbehorde_url': 'https://www.ludwigshafen.de/buergerservice/auslaenderbehoerde/',
        'termin_url': '',
        'beschreibung': "Ren kıyısında sanayi şehri, Mannheim'ın karşısında.",
    },
    {
        'name': 'Frankenthal (Pfalz)',
        'slug': 'frankenthal',
        'typ': 'kreisfrei',
        'lat': 49.5333,
        'lng': 8.3564,
        'population': 49000,
        'auslaenderbehorde_url': 'https://www.frankenthal.de/buergerservice/auslaenderbehoerde/',
        'termin_url': '',
        'beschreibung': 'Rhein-Pfalz bölgesinde küçük ve yaşanabilir bir şehir.',
    },
    {
        'name': 'Landau in der Pfalz',
        'slug': 'landau',
        'typ': 'kreisfrei',
        'lat': 49.1977,
        'lng': 8.1164,
        'population': 47000,
        'auslaenderbehorde_url': 'https://www.landau.de/buergerservice/auslaenderbehoerde/',
        'termin_url': '',
        'beschreibung': 'Pfalz bağ bölgesinin kalbinde üniversite şehri.',
    },
    {
        'name': 'Neustadt an der Weinstraße',
        'slug': 'neustadt-weinstrasse',
        'typ': 'kreisfrei',
        'lat': 49.3522,
        'lng': 8.1383,
        'population': 54000,
        'auslaenderbehorde_url': 'https://www.neustadt.eu/buergerservice/auslaenderbehoerde/',
        'termin_url': '',
        'beschreibung': 'Alman Şarap Yolu üzerinde bağcılıkla ünlü şehir.',
    },
    {
        'name': 'Pirmasens',
        'slug': 'pirmasens',
        'typ': 'kreisfrei',
        'lat': 49.2006,
        'lng': 7.6052,
        'population': 40000,
        'auslaenderbehorde_url': 'https://www.pirmasens.de/buergerservice/auslaenderbehoerde/',
        'termin_url': '',
        'beschreibung': "Pfälzerwald'ın güneybatısında sanayi geçmişiyle bilinen şehir.",
    },
    {
        'name': 'Speyer',
        'slug': 'speyer',
        'typ': 'kreisfrei',
        'lat': 49.3171,
        'lng': 8.4312,
        'population': 50000,
        'auslaenderbehorde_url': 'https://www.speyer.de/buergerservice/auslaenderbehoerde/',
        'termin_url': '',
        'beschreibung': 'UNESCO Dünya Mirası Speyer Katedrali ile tarihi Ren kıyısı şehri.',
    },
    {
        'name': 'Worms',
        'slug': 'worms',
        'typ': 'kreisfrei',
        'lat': 49.6317,
        'lng': 8.3650,
        'population': 83000,
        'auslaenderbehorde_url': 'https://www.worms.de/buergerservice/auslaenderbehoerde/',
        'termin_url': '',
        'beschreibung': "Almanya'nın en eski şehirlerinden, Nibelungen destanının kenti.",
    },
    {
        'name': 'Zweibrücken',
        'slug': 'zweibruecken',
        'typ': 'kreisfrei',
        'lat': 49.2489,
        'lng': 7.3605,
        'population': 34000,
        'auslaenderbehorde_url': 'https://www.zweibruecken.de/buergerservice/auslaenderbehoerde/',
        'termin_url': '',
        'beschreibung': 'Batı Pfalz\'da güller şehri olarak bilinen küçük şehir.',
    },
]


def add_staedte(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    for s in RLP_STAEDTE:
        Stadt.objects.get_or_create(slug=s['slug'], defaults=s)


def remove_staedte(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    slugs = [s['slug'] for s in RLP_STAEDTE]
    Stadt.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0002_seed_mainz'),
    ]

    operations = [
        migrations.RunPython(add_staedte, remove_staedte),
    ]
