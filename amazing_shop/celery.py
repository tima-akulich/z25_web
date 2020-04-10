import os
import django
from celery import Celery
from shop.tasks import SCHEDULE as SHOP_SCHEDULE


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazing_shop.settings')

django.setup()

app = Celery('amazing_shop')
app.config_from_object('django.conf.settings', namespace='CELERY')

app.conf.beat_schedule = SHOP_SCHEDULE

app.autodiscover_tasks()
