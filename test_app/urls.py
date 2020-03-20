from django.urls import path
from test_app.views import tests_index_view
from test_app.views import test_details_view
from test_app.views import search
from test_app.views import redirect


urlpatterns = [
    path('tests', tests_index_view, name='tests_view'),
    path('tests/<int:test_id>', test_details_view, name='test_details'),
    path('search', search, name='search'),
    path('redirect', redirect, name='redirect'),
]
