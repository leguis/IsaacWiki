from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    description = models.TextField()
    extension = models.CharField(max_length=200)