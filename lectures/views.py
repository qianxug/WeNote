from django.shortcuts import render, get_object_or_404, redirect 
from lectures.models import *
from .forms import NoteUploadForm
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import logging

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

def showAllNotes(request):
    selectedNote = Note.objects.all()
    context = {
        'selectedNote': selectedNote
    }
    return render(request, 'lectures/lecture-template.html', context)

def showOneNote(request, noteID):
    selectedNote = Note.objects.get(id=noteID)
    #logger.info(selectedNote.pdf)
    context = {
        'selectedNote': selectedNote,
        # 'title': selectedLecture.name
    }
    return render(request, 'lectures/note-template.html', context)

def upload(request):
    if request.method == 'POST':
        uploadedFile = request.FILES['document']
        #logger.info(request.FILES)
        # print(request.FILES)

        fs = FileSystemStorage()
        fs.save(uploadedFile.name, uploadedFile)
        # return HttpResponse('yo')
    return render(request, 'lectures/upload.html')

def uploadNote(request):
    if request.method == "POST":
        form = NoteUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/lectures/1/')
        
        else:
            form = NoteUploadForm()

    form = NoteUploadForm()
    context = {
        'form': form
    }
    return render(request, 'lectures/upload-note.html', context)