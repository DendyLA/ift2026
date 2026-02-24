from django.shortcuts import render

from .models import Intro, About, Tabs, PartnershipType, FileResource
from apps.news.models import News
from apps.speakers.models import Person as Speaker
from apps.accounts.models import CatalogEntry

def index(request):
	intro = Intro.objects.first()
	about = About.objects.first()
	tabs = Tabs.objects.all()[:3]
	partnership_types = PartnershipType.objects.prefetch_related('partners__level').all()
     
	speakers = Speaker.objects.filter(is_active=True).order_by('order')


	off_support = FileResource.objects.filter(resource_type='off_support', is_active=True)
	brochures = FileResource.objects.filter(resource_type='brochure', is_active=True)
	travel_guides = FileResource.objects.filter(resource_type='travel_guide', is_active=True)
	meet_req = FileResource.objects.filter(resource_type='meet_req', is_active=True)
	investment = FileResource.objects.filter(resource_type='investment', is_active=True)
	
	latest_news = News.objects.all()[:4]
	more_news = News.objects.all().exclude(id__in=[n.id for n in latest_news])[:5]

	catalog_entries = CatalogEntry.objects.exclude(img='').exclude(img=None)

	context = {
		'intro': intro,
		'about': about,
		'tabs': tabs,
		'partnership_types': partnership_types,
		'latest_news' : latest_news,
		'more_news' : more_news,
		'speakers': speakers,
		'off_support': off_support,
		'brochures': brochures,          
        'travel_guides': travel_guides,
        'meet_req': meet_req,
        "catalog_entries": catalog_entries,
		'investment': investment,
	}

	return render(request, 'core/index.html', context)


def privacy_policy(request):
    return render(request, 'core/docs/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'core/docs/terms_of_service.html')