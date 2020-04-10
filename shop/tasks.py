import time
from datetime import timedelta
from django.core.mail import send_mail


@shared_task
def hard_logic():
    time.sleep(5)
    return "It works!"


@shared_task
def my_periodic_logic():
    print('Run logic!!')


SCHEDULE = {
    'my_periodic_logic': {
        'task': 'shop.tasks.my_periodic_logic',
        'args': (),
        'options': {},
        'schedule': timedelta(seconds=5)
    }
}

@shared_task
def send_email_task():
    products = Products.obj.all
    send_mail(
        'New products',
        f'HelloThe list of new products:',
        'amazing.shop.test@gmail.com',
        ['mrtwister5950@mail.com']
    )