from django.db import models

class Lecture(models.Model):
    name = models.CharField(max_length=50)
    #slug = models.SlugField(unique=True)
    description = models.CharField(max_length=100)
