from django.contrib import admin

from test_app.models import Test
from test_app.models import Question
from test_app.models import Answer
from test_app.models import UserAnswer


class TestAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', '__str__', 'id')
    search_fields = ('title', 'number')
    list_display_links = ('__str__', 'id')
    list_editable = ('number', 'title')


class UserAnswerAdmin(admin.ModelAdmin):
    list_filter = ('user', 'test')


admin.site.register(Test, TestAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserAnswer, UserAnswerAdmin)
