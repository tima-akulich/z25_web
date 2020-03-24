from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from shop.forms import CardForm


from shop.models import Product


def hello_world(request):
    return HttpResponse('Hello world!')


def hello_world_template(request):
    text = request.GET.get('text', 'world')
    return render(request, 'hello_world.html', context={
        'text': text,
    })


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
