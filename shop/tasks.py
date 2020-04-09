import time
from datetime import timedelta

from celery import shared_task
from celery.schedules import crontab
from django.contrib.auth.models import User
from django.core import mail
from django.core.mail import EmailMessage
from django.utils import timezone

from amazing_shop import settings
from shop.models import Product


@shared_task
def hard_logic():
    time.sleep(5)
    return "It works!"


@shared_task
def my_periodic_logic():
    print('Run logic!!')


def mailing_dict():
    users = User.objects.all().exclude(email='')
    return {user.username: user.email for user in users}


def new_products():
    products = Product.objects.filter(
        created_at__gte=timezone.now() - timedelta(
            days=settings.NEW_PRODUCT_DAYS)
    )
    list_products = [f'{product.title}: {product.price}$' for product in
                     products]
    return '\n'.join(list_products)


@shared_task
def send_email():
    products = new_products()
    users = mailing_dict()
    messages = []
    for name, email in users.items():
        messages.append(EmailMessage(
                        'New products from amazing_shop',
                        f'Hello, {name}!\nSee what\'s new here\n{products}',
                        'anatskodr@gmail.com',
                        [email]))
    connection = mail.get_connection()
    connection.send_messages(messages)


SCHEDULE = {
    'my_periodic_logic': {
        'task': 'shop.tasks.my_periodic_logic',
        'args': (),
        'options': {},
        'schedule': timedelta(seconds=30)
    },
    'send_email': {
        'task': 'shop.tasks.send_email',
        'args': (),
        'options': {},
        'schedule': crontab(minute='16', hour='10', day_of_week='fri')
    }
}
