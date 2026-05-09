from django.db import migrations

ARMA_URLS = {
    'BY': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Coat_of_arms_of_Bavaria.svg/960px-Coat_of_arms_of_Bavaria.svg.png',
    'NI': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Coat_of_arms_of_Lower_Saxony.svg/960px-Coat_of_arms_of_Lower_Saxony.svg.png',
    'BB': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Coat_of_arms_of_Brandenburg.svg/960px-Coat_of_arms_of_Brandenburg.svg.png',
    'MV': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Coat_of_arms_of_Mecklenburg-Vorpommern.svg/960px-Coat_of_arms_of_Mecklenburg-Vorpommern.svg.png',
    'SH': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Coat_of_arms_of_Schleswig-Holstein.svg/960px-Coat_of_arms_of_Schleswig-Holstein.svg.png',
    'SL': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Coat_of_arms_of_Saarland.svg/960px-Coat_of_arms_of_Saarland.svg.png',
    'SN': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Coat_of_arms_of_Saxony.svg/960px-Coat_of_arms_of_Saxony.svg.png',
    'ST': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Coat_of_arms_of_Saxony-Anhalt.svg/960px-Coat_of_arms_of_Saxony-Anhalt.svg.png',
    'TH': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Coat_of_arms_of_Thuringia.svg/960px-Coat_of_arms_of_Thuringia.svg.png',
}


def fill_arma_urls(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    for kod, url in ARMA_URLS.items():
        Eyalet.objects.filter(kod=kod, arma_url='').update(arma_url=url)


def reverse_fill(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    for kod in ARMA_URLS:
        Eyalet.objects.filter(kod=kod).update(arma_url='')


class Migration(migrations.Migration):
    dependencies = [
        ('stadt', '0043_hannover_action_links_aktiv'),
    ]
    operations = [
        migrations.RunPython(fill_arma_urls, reverse_fill),
    ]
