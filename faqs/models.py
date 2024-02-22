from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=254, null=False, blank=False)
    answer = models.TextField(null=False, blank=False)
