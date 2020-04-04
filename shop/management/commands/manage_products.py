from django.core.management import BaseCommand

from shop.models import Product


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--ids', required=True, help='Product ids')
        parser.add_argument('--unpublish', action='store_true')

    def handle(self, *args, **options):
        ids = [int(_id) for _id in options['ids'].split(',')]
        if options['unpublish']:
            Product.objects.filter(id__in=ids).update(published=False)
