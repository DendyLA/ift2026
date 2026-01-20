from django.shortcuts import render
from .models import Intro, About, Tabs, PartnershipType
from apps.news.models import News

def index(request):
	intro = Intro.objects.first()
	about = About.objects.first()
	tabs = Tabs.objects.all()[:3]
	partnership_types = PartnershipType.objects.prefetch_related('partners__level').all()
     
	latest_news = News.objects.all()[:4]
	more_news = News.objects.all().exclude(id__in=[n.id for n in latest_news])[:5]

	context = {
		'intro': intro,
        'about': about,
        'tabs': tabs,
		'partnership_types': partnership_types,
        'latest_news' : latest_news,
        'more_news' : more_news
	}

	return render(request, 'core/index.html', context)


def privacy_policy(request):
    return render(request, 'core/docs/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'core/docs/terms_of_service.html')