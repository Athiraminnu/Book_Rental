from django.contrib import messages
from django.http import Http404
from django.shortcuts import render
from . models import Category, Books
# Create your views here.


def dashboard(request):
    book = Books.objects.all()
    return render(request, "dashboard.html", {'data': book})


def fiction(request):
    try:
        fictionCategory = Category.objects.get(name='FICTION')
        fictionBook = Books.objects.filter(var=fictionCategory)
    except Category.DoesNotExist:
        messages.error(request, "Fiction category doesnot exist!!!")
    return render(request, "fiction.html", {'fbooks': fictionBook})


def anime(request):
    try:
        animeCategory = Category.objects.get(name='anime')
        animeBooks = Books.objects.filter(var=animeCategory)
    except Category.DoesNotExist:
        messages.error(request, "anime category doesnot exist!!!")
    return render(request, 'anime.html', {'abooks': animeBooks})


def horror(request):
    try:
        horrorCategory = Category.objects.get(name='horror')
        horrorBooks = Books.objects.filter(var=horrorCategory)
    except Category.DoesNotExist:
        messages.error(request, "Horror category doesnot exist!!!")
        horrorBooks = []

    return render(request, 'horror.html', {'hbooks': horrorBooks})