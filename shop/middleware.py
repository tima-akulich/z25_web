from django.utils.deprecation import MiddlewareMixin
from .models import Error505


def my_exception_middleware(get_response):
    def middleware(request):
        print('Before 1')
        response = get_response(request)
        if response.status_code == 500:
            print('server error')
        print('After 1')
        return response
    return middleware


class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Before 2')
        response = self.get_response(request)
        print('After 2')
        return response


class Hook500Error:
    def __init(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if str(response.status_code).startswith('5'):
            Error505.objects.create(status_code=response.status_code, body='500+Error')
        return response
