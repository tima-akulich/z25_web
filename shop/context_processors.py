from contextlib import suppress

from django.conf import settings

from shop.models import Basket


def new_setting(request):
    return {
        'NEW_SETTINGS': settings.NEW_SETTINGS
    }


def user_added_products(request):
    product_ids = set()
    if request.user.is_authenticated:
        with suppress(Basket.DoesNotExist):
            basket = Basket.objects.filter(
                user=request.user
            ).latest('updated_at')
            product_ids = set(basket.items.all().values_list(
                'product_id', flat=True
            ))
    return {
        'user_product_ids': product_ids
    }
