import time
from datetime import timedelta, datetime
from celery.schedules import crontab

from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from django.template.loader import get_template



from shop.models import Product


@shared_task
def hard_logic():
    time.sleep(5)
    return "It works!"


@shared_task
def my_periodic_logic():
    print('Run logic!!')


@shared_task
def new_products_email():
    new_products_ids = set(Product.objects.filter(
        created_at__gte=datetime.now() - timedelta(
            days=settings.NEW_PRODUCTS_DAYS)
    ).values_list('id', flat=True))
    UserModel = get_user_model()
    users = UserModel.objects.exclude(email='').prefetch_related(
        'baskets',
        'baskets__items',
        'baskets__orders'
    )
    users_products = {}
    for user in users:
        for basket in user.baskets.all():
            users_products.setdefault(user.id, set())
            if len(basket.orders.all()):
                users_products[user.id].update(
                    basket.items.all().values_list('product_id', flat=True)
                )
    for user_id, user_products_ids in users_products.items():
        new_user_products = new_products_ids - user_products_ids
        if new_user_products:
            send_user_email.delay(user_id, list(new_user_products))


@shared_task
def send_user_email(user_id, product_ids):
    user = get_user_model().objects.get(id=user_id)
    products = Product.objects.filter(id__in=product_ids)
    template = get_template('email.html')

    email_message = ''
    for product in products:
        email_message += f'{product.title} - {product.price}\n'
    send_mail(
        subject='New products',
        message=email_message,
        from_email=settings.ADMIN_EMAIL,
        recipient_list=[user.email],
        html_message=template.render(context={
            'user': user,
            'products': products
        })
    )


SCHEDULE = {
    'my_periodic_logic': {
        'task': 'shop.tasks.my_periodic_logic',
        'args': (),
        'options': {},
        'schedule': timedelta(seconds=5)
    },
    'new_products_email': {
        'task': 'shop.tasks.new_products_email',
        'args': (),
        'options': {},
        # 'schedule': crontab(day_of_week='mon', hour=9, minute=0),
        'schedule': timedelta(seconds=5),
    }
}
