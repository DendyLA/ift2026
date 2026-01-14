from django.shortcuts import render, get_object_or_404

from .models import News

def news(request):
	news = News.objects.all()

	context = {
		'news': news,
	}

	return render(request, 'news/news.html', context)


def newsDetail(request, slug):
	news = get_object_or_404(News, slug=slug)
	latestNews = News.objects.exclude(id=news.id).order_by('-date')[:3]

	context = {
		'news' : news,
		'latest_news': latestNews
	}

	return render(request, 'news/news_detail.html', context)