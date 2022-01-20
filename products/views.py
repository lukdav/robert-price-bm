from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view to return all products, including sorting and searching functionality. """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
