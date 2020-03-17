from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('Hello world!')


def hello_world_template(request):
    text = request.GET.get('text', 'world')
    return render(request, 'hello_world.html', context={
        'text': text
    })
