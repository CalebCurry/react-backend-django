from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)
