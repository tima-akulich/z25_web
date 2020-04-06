import traceback

from django.utils.deprecation import MiddlewareMixin
<<<<<<< HEAD
from .models import Error505
=======
from shop.models import RequestError
>>>>>>> d7cffe717e0a719dd5bf666ed4c3b6acbd90c6d0


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


<<<<<<< HEAD
class Hook500Error:
    def __init(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if str(response.status_code).startswith('5'):
            Error505.objects.create(status_code=response.status_code, body='500+Error')
        return response
=======
class LogExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        RequestError.objects.create(
            exception_name=str(type(exception)),
            exception_value=str(exception),
            exception_tb='\n'.join(traceback.format_tb(exception.__traceback__)),  # noqa
            request_method=request.method,
            path=request.path,
            query=dict(request.GET),
            data=dict(request.POST)
        )
>>>>>>> d7cffe717e0a719dd5bf666ed4c3b6acbd90c6d0
