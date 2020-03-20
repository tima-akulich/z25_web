from django.shortcuts import render


def checkparentheses(request):
    text = request.GET.get('text')
    counter = 0
    if text:
        for i in text:
            if counter < 0:
                break
            else:
                if i == '(':
                    counter += 1
                elif i == ')':
                    counter -= 1
        result = 'right' if counter == 0 else 'wrong'
    else:
        result = "no text"
    return render(request, 'form.html', context={'result': result})
