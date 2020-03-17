from django.db import models


class MyFirstModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    text_column = models.TextField(null=True)
    bool_column = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    bin_column = models.BinaryField(null=True)
    email_column = models.EmailField(null=True)
    number_column = models.PositiveIntegerField(default=0)
