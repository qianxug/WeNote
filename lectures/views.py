from django.shortcuts import render, get_object_or_404
from lectures.models import *
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
# import logging

# Create your views here.

def home(request):
    print('hi')
    return render(request, 'lectures/index.html')

def showAllLectures(request):
    selectedLecture = Lecture.objects.all()
    context = {
        'selectedLecture': selectedLecture,
        # 'title': 'All Lectures for CLASS'
    }
    return render(request, 'lectures/all-lectures.html', context)

def showOneLecture(request, lecID):
    selectedLecture = Lecture.objects.get(id=lecID)
    context = {
        'selectedLecture': selectedLecture,
        # 'title': selectedLecture.name
    }
    return render(request, 'lectures/lecture-template.html', context)

def upload(request):
    if request.method == 'POST':
        uploadedFile = request.FILES['document']
        #logger.info(request.FILES)
        # print(request.FILES)

        fs = FileSystemStorage()
        fs.save(uploadedFile.name, uploadedFile)
        # return HttpResponse('yo')
    return render(request, 'lectures/upload.html')