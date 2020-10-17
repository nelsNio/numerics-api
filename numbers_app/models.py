from django.db import models


# Create your models here.
class NumberSort(models.Model):
    numbers = models.JSONField()
