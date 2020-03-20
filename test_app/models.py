from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Questions(models.Model):
    number = models.IntegerField()
    text = models.TextField(max_length=100)


class Tests(models.Model):
    number = models.IntegerField()
    text = models.TextField(max_length=100)
    question = models.ManyToManyField(Questions)


class Answers(models.Model):
    text = models.TextField(max_length=100)
    is_correct = models.BooleanField(default=False)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)


class UsersAnswers(models.Model):
    questions_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'questions_id')
