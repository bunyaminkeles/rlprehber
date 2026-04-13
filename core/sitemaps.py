from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import BlogYazisi
from rehber.models import Kaynak
from stadt.models import Stadt
from almanca.engine import konu_listesi


class StatikSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return [
            'core:anasayfa',
            'core:hakkinda',
            'core:iletisim',
        ]

    def location(self, item):
        return reverse(item)


class StadtSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Stadt.objects.filter(aktiv=True).select_related('eyalet')

    def location(self, obj):
        eyalet_slug = obj.eyalet.slug if obj.eyalet else 'rlp'
        return f'/{eyalet_slug}/{obj.slug}/'


class AlmancaSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return [k['slug'] for k in konu_listesi()]

    def location(self, slug):
        return f'/rlp/almanca/{slug}/'


class BlogSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return BlogYazisi.objects.filter(yayinda=True, scope='eyalet').select_related('eyalet')

    def lastmod(self, obj):
        return obj.olusturulma

    def location(self, obj):
        return obj.canonical_url


class StadtBlogSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return BlogYazisi.objects.filter(yayinda=True, scope='stadt').select_related('stadt__eyalet', 'eyalet')

    def lastmod(self, obj):
        return obj.olusturulma

    def location(self, obj):
        return obj.canonical_url


class RehberSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Kaynak.objects.filter(yayinda=True, scope='eyalet', tip='sayfa').exclude(slug=None).exclude(slug='')

    def lastmod(self, obj):
        return obj.guncelleme

    def location(self, obj):
        return '/rlp/rehber/{}/'.format(obj.slug)


SITEMAPS = {
    'statik':     StatikSitemap,
    'staedte':    StadtSitemap,
    'almanca':    AlmancaSitemap,
    'blog':       BlogSitemap,
    'stadt-blog': StadtBlogSitemap,
    'rehber':     RehberSitemap,
}
