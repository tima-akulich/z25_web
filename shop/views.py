from django.shortcuts import render, get_object_or_404

from shop.models import Product
from shop.models import Category


def products_list_view(request, category=None):
    products = Product.objects.filter(published=True)
    if category:
        products = products.filter(categories__slug=category)
    return render(request, 'products_list.html', context={
        'products': products,
    })


def product_details_view(request, pk):
    product = get_object_or_404(Product, pk=pk, published=True)
    return render(request, 'product_details.html', context={
        'product': product,
    })


def categories_view(request):
    categories = Category.objects.filter()
    for category in categories:
        category.products = category.product_set.all()
    return render(request, 'categories.html', context={
        'categories': categories,
    })
