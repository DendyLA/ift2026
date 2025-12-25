from django.shortcuts import render
from .models import Intro

def index(request):
	intro = Intro.objects.first()

	context = {
		'intro': intro,
	}

	return render(request, 'core/index.html', context)


def privacy_policy(request):
    return render(request, 'core/docs/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'core/docs/terms_of_service.html')