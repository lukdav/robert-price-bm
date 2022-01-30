from django.shortcuts import render

from .models import Blog

def blog_posts(request):
    """ A view to return the blog """
    all_posts = Blog.objects.all()

    template = 'blog/blog.html'
    context = {
        'all_posts': all_posts,
    }

    return render(request, template, context)
