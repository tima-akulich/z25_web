from django.shortcuts import render


def check_parentheses(request):
    input_text = request.GET.get('input_text', '')
    counter = 0
    for sym in input_text:
        if sym == '(':
            counter += 1
        elif sym == ')':
            counter -= 1
        if counter < 0:
            break
    return render(request, 'index.html', context={
        'input_text': input_text,
        'response_text': 'Correct' if not counter else 'Incorrect!',
        'user_agent': request.META['HTTP_USER_AGENT']
    })
