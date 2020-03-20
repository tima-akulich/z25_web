from django.db import models

# Create your models here.


# насколько я понимаю "blank=False" дефолтное значение
class Appusers(models.Model):
    username = models.CharField(max_length=30, unique=True, blank=False)


class Tests(models.Model):
    number = models.IntegerField(blank=False)
    text = models.CharField(max_length=100, blank=False, unique=True)


# test_id - это к какому тесту принадлежит вопрос
class Questions(models.Model):
    number = models.IntegerField(blank=False)
    text = models.CharField(max_length=100, blank=False, unique=True)
    test_id = models.ManyToManyField(Tests)


class tests_questions(models.Model):
    test_id = models.ForeignKey(Tests, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("test_id", "question_id")


class Answers(models.Model):
    text = models.CharField(max_length=100, blank=False)
    is_correct = models.BooleanField(default=False)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)


class Useranswers(models.Model):
    tests_questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Appusers, on_delete=models.CASCADE)
    answers_id = models.ForeignKey(Answers, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user_id", "tests_questions")
