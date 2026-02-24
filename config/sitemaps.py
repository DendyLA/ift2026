from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import translation
from django.conf import settings
from apps.core.models import About, Partner, Sector, Sponsor
from apps.news.models import News


class MultiLangSitemap(Sitemap):
    """
    Базовый класс для мультиязычных объектов:
    генерирует URL для всех языков и поддерживает hreflang.
    """

    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        raise NotImplementedError("Override this method in child class")

    def location(self, item):
        """
        Генерируем URL для конкретного языка.
        item = {'obj': object_or_urlname, 'lang': lang_code, 'kwargs': optional_kwargs}
        """
        obj_or_name = item.get('obj')
        lang = item.get('lang', settings.LANGUAGE_CODE)
        kwargs = item.get('kwargs', {})

        with translation.override(lang):
            # Если объект модели имеет get_absolute_url — используем его
            if hasattr(obj_or_name, 'get_absolute_url'):
                return obj_or_name.get_absolute_url()
            # Если передан URL name — используем reverse
            if isinstance(obj_or_name, str):
                return reverse(obj_or_name, kwargs=kwargs)
            raise ValueError(f"Invalid item for sitemap: {obj_or_name}")

    def alternates(self, item):
        """
        Возвращает URL для всех языков для hreflang
        """
        alternates = {}
        for lang_code, _ in settings.LANGUAGES:
            alternates[lang_code] = self.location({
                'obj': item.get('obj'),
                'lang': lang_code,
                'kwargs': item.get('kwargs', {})
            })
        return alternates


# -------------------
# Статические страницы
# -------------------

class StaticViewSitemap(MultiLangSitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        urls = []
        real_urls = [
            'core:index',
            'core:privacy_policy',
            'core:terms_of_service',
            'news:news'
        ]
        for lang_code, _ in settings.LANGUAGES:
            for url_name in real_urls:
                urls.append({'obj': url_name, 'lang': lang_code})
        return urls


# -------------------
# About
# -------------------

class AboutSitemap(MultiLangSitemap):
    priority = 0.7
    changefreq = 'monthly'

    def items(self):
        items = []
        for obj in About.objects.all():
            for lang_code, _ in settings.LANGUAGES:
                items.append({'obj': obj, 'lang': lang_code})
        return items


# -------------------
# News
# -------------------

class NewsSitemap(MultiLangSitemap):
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        items = []
        for obj in News.objects.all():
            for lang_code, _ in settings.LANGUAGES:
                items.append({
                    'obj': 'news:detail',   # вот тут используем URL name
                    'lang': lang_code,
                    'kwargs': {'slug': obj.slug}
                })
        return items

    def lastmod(self, item):
        # item = {'obj': url_name, 'lang': lang_code, 'kwargs': {...}}
        # нам нужен объект для даты, поэтому храним slug
        slug = item['kwargs']['slug']
        try:
            news_obj = News.objects.get(slug=slug)
            return news_obj.date
        except News.DoesNotExist:
            return None
