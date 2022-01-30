from django.shortcuts import render


def blog_posts(request):
    """ A view to return the blog """
    template = 'blog/blog.html'
    context = {}

    return render(request, template, context)
