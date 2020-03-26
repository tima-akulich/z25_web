from django.conf import settings


def new_setting(request):
    return {
        'NEW_SETTINGS': settings.NEW_SETTINGS
    }
