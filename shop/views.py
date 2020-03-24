from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product


def hello_world(request):
    return HttpResponse('Hello world!')


def hello_world_template(request):
    text = request.GET.get('text', 'world')
    return render(request, 'hello_world.html', context={
        'text': text
    })


def products(request):
    return render(request, 'products.html', context={'prod_list': Product.objects.all()})


def product_information(request):
    lst = Product.objects.all()
    for elem in lst:
        return render(request, 'product_extensions.html', context={
            'product_name': elem.name,
            'x': elem
        })


