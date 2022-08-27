from django.db import models

class Lecture(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    numNotes = models.FloatField()

class Note(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    format = models.CharField(max_length=10)
    numVotes = models.FloatField()


class Lecture2(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    numNotes = models.FloatField(default=None)