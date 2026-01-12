from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.core.models import Intro, Partner, Tabs, About
from apps.about.models import Gallery

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['core:index', 'about:about']

    def location(self, item):
        return reverse(item)


class AboutSitemap(Sitemap):
    priority = 0.7
    changefreq = 'monthly'

    def items(self):
        return About.objects.all()

    def location(self, obj):
        # Если есть get_absolute_url() у модели, используем его
        return obj.get_absolute_url()


class PartnerSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Partner.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()