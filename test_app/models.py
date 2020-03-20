from django.db import models

# CREATE TABLE app_users (
#     id SERIAL PRIMARY KEY,
#     username VARCHAR(30) UNIQUE NOT NULL
# );
#
# CREATE TABLE tests (
#     id SERIAL PRIMARY KEY,
#     number SMALLINT NOT NULL,
#     text VARCHAR(100) NOT NULL
# );
#
# CREATE TABLE questions (
#     id SERIAL PRIMARY KEY,
#     number SMALLINT NOT NULL,
#     text VARCHAR(100) NOT NULL
# );
#
# CREATE TABLE tests_questions (
#     id SERIAL PRIMARY KEY,
#     test_id INTEGER REFERENCES tests(id),
#     question_id INTEGER REFERENCES questions(id),
#     UNIQUE (test_id, question_id)
# );
#
# CREATE TABLE answers (
#     id SERIAL PRIMARY KEY,
#     text VARCHAR(100) NOT NULL,
#     is_correct BOOL DEFAULT FALSE,
#     question_id INTEGER REFERENCES questions(id)
# );
#
# CREATE TABLE users_answers (
#     id SERIAL PRIMARY KEY,
#     tests_questions_id INTEGER REFERENCES tests_questions(id),
#     user_id INTEGER REFERENCES app_users(id),
#     answer_id INTEGER REFERENCES answers(id),
#     UNIQUE (tests_questions_id, user_id)
# );


class AppUsers(models.Model):
    username = models.CharField(max_length=30, unique=True)


class Tests(models.Model):
    number = models.PositiveSmallIntegerField(default=0)
    text = models.CharField(max_length=100)


class Questions(models.Model):
    number = models.PositiveSmallIntegerField(default=0)
    text = models.CharField(max_length=100)
    tests = models.ManyToManyField(Tests)


class Answers(models.Model):
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)


class UsersAnswers(models.Model):
    user_id = models.ForeignKey(AppUsers, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE)
    answers = models.CharField(max_length=100)
