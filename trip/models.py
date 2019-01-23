from django.conf import settings
from django.db import models
from django.utils import timezone


class Cities(models.Model):
    city_name = models.CharField(max_length=200)
    def __str__(self):
        return self.city_name
