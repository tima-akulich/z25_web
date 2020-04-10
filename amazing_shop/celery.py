import os
import django

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazing_shop.settings')
django.setup()

from shop.tasks import SCHEDULE as SHOP_SCHEDULE

app = Celery('amazing_shop')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = SHOP_SCHEDULE

app.autodiscover_tasks()
