from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from shop.forms import CardForm
from django.core.paginator import Paginator

from shop.models import Product, Category


def products_list_view(request):
    products = Product.objects.filter(published=True)
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'list.html', context=context)


def product_details_view(request, pk):
    product = get_object_or_404(Product, pk=pk, published=True)
    return render(request, 'product_details.html', context={
        'product': product,
    })


def index(request):
    return render(request, 'base.html')


def try_forms(request):
    form = CardForm()
    if request.POST:
        form = CardForm(request.POST)
        if form.is_valid():
            print('Clean data', form.cleaned_data)
        else:
            print('Errors', form.errors)
    return render(request, 'try_forms.html', context={
        'form': form
    })


def categories(request):
    cats = Category.objects.all()
    return render(request, 'categories.html', context={
        'categories': cats
    })


def products_by_category(request):
    category = request.GET.get('category', '')
    if not category:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(categories=category)
    context = {
        'products': products,
    }
    return render(request, 'product_by_category_list.html', context=context)
