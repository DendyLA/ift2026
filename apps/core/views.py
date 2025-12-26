from django.shortcuts import render
from .models import Intro, About, Tabs, PartnershipType

def index(request):
	intro = Intro.objects.first()
	about = About.objects.first()
	tabs = Tabs.objects.all()[:3]
	partnership_types = PartnershipType.objects.prefetch_related('partners__level').all()


	context = {
		'intro': intro,
        'about': about,
        'tabs': tabs,
		'partnership_types': partnership_types,
	}

	return render(request, 'core/index.html', context)


def privacy_policy(request):
    return render(request, 'core/docs/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'core/docs/terms_of_service.html')