import time
from datetime import timedelta

from celery import shared_task


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
