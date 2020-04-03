from django.utils.deprecation import MiddlewareMixin

from shop.models import ServerError


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


class ServerErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 500:
            error = ServerError(
                method=request.method,
                path=request.path,
                data=request.get(request.method),
                response=response
            )
            error.save()
        return response
