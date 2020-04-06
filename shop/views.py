from contextlib import suppress
from datetime import timedelta

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.generic import TemplateView, ListView, DetailView, FormView

from shop.forms import ProductForm, RegistrationForm, BasketEditForm
from shop.models import Product, Category, Basket, BasketItem


@csrf_exempt
@require_http_methods(['GET', 'HEAD', 'DELETE', 'PUT'])
def category_root_view(request):
    first_category = Category.objects.first()
    if not first_category:
        raise Http404
    return redirect(reverse('products_by_category', kwargs={
        'category': first_category.slug
    }))


def products_list_view(request, category=None):
    products = Product.objects.filter(
        published=True
    ).prefetch_related('images')
    template_name = 'products_list.html'
    if category:
        template_name = 'categories.html'
        products = products.filter(categories__slug=category)

    paginator = Paginator(products, settings.PAGE_SIZE)
    page_number = request.GET.get('page', 1)

    products = paginator.get_page(page_number)

    return render(request, template_name, context={
        'categories': Category.objects.all(),
        'products': products,
        'selected_category': category
    })


@login_required
def product_details_view(request, pk):
    product = get_object_or_404(Product, pk=pk, published=True)
    return render(request, 'product_details.html', context={
        'product': product,
    })


class ProductDetail(DetailView):
    template_name = 'product_details.html'
    queryset = Product.objects.filter(published=True)


class TryCBV(TemplateView):
    template_name = 'try_cbv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_var'] = 1000
        return context

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductsList(LoginRequiredMixin, ListView):
    template_name = 'products_list.html'
    paginate_by = settings.PAGE_SIZE

    def get_template_names(self):
        templates = super().get_template_names()
        if self.kwargs.get('category'):
            templates = ['categories.html']
        return templates

    def get_queryset(self):
        products = Product.objects.filter(
            published=True
        ).prefetch_related('images')
        category = self.kwargs.get('category')
        if category:
            products = products.filter(categories__slug=category)
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['selected_category'] = self.kwargs.get('category')
        context['categories'] = Category.objects.all()
        return context


class ProductFormView(FormView):
    template_name = 'product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.save()
        if self.request.GET.get("exception"):
            raise Exception("ERROR!")
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


@login_required
def product_form_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('products'))
        else:
            pass
    return render(request, 'product_form.html', context={
        'form': form
    })


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.save()
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        login(self.request, user)
        return super().form_valid(form)


class BasketEditView(LoginRequiredMixin, FormView):
    http_method_names = ['post']
    form_class = BasketEditForm

    def form_valid(self, form):
        Basket.objects.filter(
            user=self.request.user,
            updated_at__lt=timezone.now() - timedelta(
                days=settings.BASKET_STORE_DAYS
            )
        ).delete()
        try:
            basket = Basket.objects.filter(
                user=self.request.user
            ).latest('updated_at')
        except Basket.DoesNotExist:
            basket = Basket.objects.create(user=self.request.user)

        product_id = form.cleaned_data['product_id']
        basket_item = basket.items.filter(
            product_id=product_id
        ).first()
        if basket_item:
            basket_item.delete()
        else:
            BasketItem.objects.create(
                basket=basket,
                product_id=product_id
            )
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER') \
               or reverse_lazy('products')


class BasketView(LoginRequiredMixin, TemplateView):
    template_name = 'basket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with suppress(Basket.DoesNotExist):
            context['basket'] = Basket.objects.filter(
                user=self.request.user
            ).prefetch_related('items').latest('updated_at')
        return context
