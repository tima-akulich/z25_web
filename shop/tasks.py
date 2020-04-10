import time
from datetime import timedelta
from celery import shared_task
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from shop.models import get_user_model
from shop.models import Product

@shared_task()
def hard_logic():
    time.sleep(5)
    return 'It works'


@shared_task
def my_periodic_logic():
    print('Run Logic!')


@shared_task
def send_email():
    new_prods = Product.objects.all()[:-5]
    subject = 'New products'
    users_emails = get_user_model().objects.filter(email=True)
    send_mail(subject, f'New products: {new_prods}', 'my_email@mail.ru', [users_emails])


SCHEDULE = {
    'my_periodic_task': {
        'task': 'shop.tasks.my_periodic_task',
        'args': (),
        'options': {},
        'schedule': timedelta(seconds=5)
    },
    'send_email': {
        'task': 'shop.tasks.send_email',
        'args': (),
        'options': {},
        'schedule': timedelta(days=7)
    }
}
