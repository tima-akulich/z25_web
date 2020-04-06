from django import template

register = template.Library()


def product_exists(products_ids, product_id):
    return product_id in products_ids


register.filter('product_exists', product_exists)
