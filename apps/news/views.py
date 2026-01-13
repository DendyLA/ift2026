from django.shortcuts import render


def news(request):


	# context = {
	# 	'gallery': gallery,
	# }

	return render(request, 'news/news.html', )
