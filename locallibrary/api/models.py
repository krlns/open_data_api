from django.db import models


class Cinema(models.Model):
    name = models.CharField(max_length=50)
    full_address = models.CharField(max_length=200, blank=True, default='')
    email = models.CharField(max_length=50, blank=True, default='')
    phone = models.CharField(max_length=11, blank=True, default='')
