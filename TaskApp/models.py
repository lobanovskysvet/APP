from django.db import models


class Users(models.Model):
    email = models.EmailField(max_length=70, blank=True)
    password = models.CharField(max_length=70, blank=True)
    first = models.CharField(max_length=25, blank=True)
    last = models.CharField(max_length=25, blank=True)
