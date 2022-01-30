from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from .models import NewsPost

from .forms import NewsPostForm




def all_news(request):
    """ A view to show all news articles """

    news = NewsPost.objects.all()

    context = {
        'news': news,
    }

    return render(request, 'news/news.html', context)


def news_article(request, slug):
    """ A view to show individual news articles """

    article = get_object_or_404(NewsPost, slug=slug)

    context = {
        'article': article,
    }

    return render(request, 'news/news_article.html', context)


