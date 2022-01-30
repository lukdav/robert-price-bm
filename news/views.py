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


# @login_required
# def add_article(request):
#     """ A view to add articles to news """

#     if not request.user.is_superuser:
#         messages.error(request, 'Only Robert Price staff are able to add new articles.')
#         return redirect(reverse('home'))

#     if request.method == 'POST':
#         form = NewsPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_post = form.save(commit=False)
#             new_post.author = request.user
#             new_post.slug = slugify(new_post.title)
#             new_post.save()
#             messages.success(request, 'Your article has been posted!')
#             return redirect(reverse('news_article', args=[new_post.slug]))
#         else:
#             messages.error(request, 'Failed to post the article. Check if the article is valid and try again.')
#     else:
#         form = NewsPostForm()

#     context = {
#         'form': form,
#     }

#     return render(request, 'news/add_article.html', context)
