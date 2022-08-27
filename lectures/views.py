from django.shortcuts import render, get_object_or_404
from lectures.models import *
from django.http import HttpResponse

# Create your views here.
 
def home(request):
    return render(request, 'lectures/index.html')

def showAllLectures(request):
    selectedLecture = Lecture.objects.all()
    context = {
        'selectedLecture': selectedLecture,
        'title': 'All Lectures for CLASS'
    }
    return render(request, 'lectures/all-lectures.html', context)

def showOneLecture(request, lecID):
    selectedLecture = Lecture.objects.get(id=lecID)
    context = {
        'selectedLecture': selectedLecture,
        'title': selectedLecture.name
    }
    return render(request, 'lectures/lecture-template.html', context)