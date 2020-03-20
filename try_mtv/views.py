from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('Hello World')


def is_correct(request):
    text = request.GET.get('text')
    counter = 0
    if text is not None:
        for i in text:
            if counter >= 0:
                if i == "(":
                    counter += 1
                elif i == ")":
                    counter -= 1
            else:
                break
        if counter == 0:
            answer = "верно"
        else:
            answer = "неверно"
    else:
        answer = "не"

    return render(request, 'MyFormHTML.html', context={
        'is_correct': answer
    })
