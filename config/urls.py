from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.template.loader import render_to_string
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, AboutSitemap, PartnerSitemap


@require_GET
def robots_txt(request):
    text = render_to_string("core/robots.txt")
    return HttpResponse(text, content_type="text/plain")


sitemaps = {
    'static': StaticViewSitemap,
    'about': AboutSitemap,
    'partners': PartnerSitemap,
}


urlpatterns = [
    path("robots.txt", robots_txt),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
     path('ckeditor/', include('ckeditor_uploader.urls')),
    path('i18n/', include('django.conf.urls.i18n')),  # для смены языка через POST
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
	path('accounts/', include('allauth.urls')),
     
    path('', include(('apps.core.urls', 'core'), namespace='core')),  # namespace
	path('profile/', include(('apps.accounts.urls', 'accounts'), namespace='accounts')),
    path('about/', include(('apps.about.urls', 'about'), namespace='about')),
     path('news/', include(('apps.news.urls', 'news'), namespace='news')),
    
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)