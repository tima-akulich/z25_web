from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    title = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField()
    questions = models.ManyToManyField('test_app.Question', blank=True)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ('number', 'title')

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField()
    number = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey('test_app.Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.test} - {self.answer.question} {self.answer}'

    class Meta:
        unique_together = (
            ('test', 'answer'),
        )
