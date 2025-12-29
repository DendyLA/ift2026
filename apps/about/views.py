from django.shortcuts import render
from .models import Gallery

def about_view(request):
	gallery = Gallery.objects.all()

	context = {
		'gallery': gallery,
	}

	return render(request, 'about/about.html', context)
