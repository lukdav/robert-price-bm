from django.shortcuts import render
from .models import NewsPost


def all_news(request):
    """ A view to show all news articles """

    news = NewsPost.objects.all()

    context = {
        'news': news,
    }

    return render(request, 'news/news.html', context)
