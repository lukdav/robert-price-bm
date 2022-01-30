from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify

from .models import Blog

def blog_posts(request):
    """ A view to return all blog posts """
    all_posts = Blog.objects.all()

    template = 'blog/blog.html'
    context = {
        'all_posts': all_posts,
    }

    return render(request, template, context)


def blog_detail(request, slug):
    """ A view to return individual blog posts """
    post = get_object_or_404(Blog, slug=slug)

    template = 'blog/blog_detail.html'
    context = {
        'post': post,
    }

    return render(request, template, context)
