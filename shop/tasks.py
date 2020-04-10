import time
from datetime import timedelta
from celery.schedules import crontab
from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
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


@shared_task
def email():
    products = Product.objects.filter(
        created_at__lt=timezone.now() - timedelta(
            days=settings.EMAIL_DAYS)
    )
    prod_list = '\n'.join([f'{product.title}: {product.price}' for product in products])
    users = User.objects.all()
    subject = 'Hello, take a look at new products!'
    message = f'New products in shop: {prod_list}'
    email_from = 'admin@gmail.com'
    recipient_list = [f'{user.email}' for user in users]
    send_mail(subject, message, email_from, recipient_list )


SCHEDULE = {
    'my_periodic_logic': {
        'task': 'shop.tasks.my_periodic_logic',
        'args': (),
        'options': {},
        'schedule': timedelta(seconds=5)
    },
    'email': {
        'task': 'shop.tasks.email',
        'args': (),
        'options': {},
        'schedule': crontab(hour=9, minute=00, day_of_week=1)
    },
}
