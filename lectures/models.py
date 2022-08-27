from django.db import models

formatChoices = (('TYPED', 'typed'), ('HANDWRITTEN','handwritten'), ('UNSPECIFIED','unspecified'))

class Lecture(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    numNotes = models.FloatField()

class Note(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    format = models.CharField(choices=formatChoices, default='unspecified', max_length=50)
    numVotes = models.FloatField(default=0)
    pdf = models.FileField(default='../media/test.pdf', upload_to='uploads')

    def __str__(self):
        return self.name


class Lecture2(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    numNotes = models.FloatField(default=None)