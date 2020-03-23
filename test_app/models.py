from django.db import models

# Create your models here.


class AppUser(models.Model):
    username = models.CharField(max_length=30, unique=True)


class Question(models.Model):
    number = models.SmallIntegerField(null=False)
    text = models.CharField(max_length=100)


class Test(models.Model):
    number = models.SmallIntegerField(null=False)
    text = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)

