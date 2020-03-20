from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from test_app.models import Test


def tests_index_view(request):
    tests = Test.objects.all().prefetch_related('questions')
    return render(request, 'index.html', context={
        'tests': tests
    })


def test_details_view(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    return render(request, 'test_details.html', context={
        'test_id': test_id,
        'test': test
    })


def search(request):
    query = request.GET.get('query', '')
    return HttpResponseRedirect(f'https://www.google.com/search?q={query}')


def redirect(request):
    return HttpResponsePermanentRedirect('https://www.google.com/')

