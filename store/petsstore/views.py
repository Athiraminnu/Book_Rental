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
        raise Http404("Fiction category does not exist")
    return render(request, "fiction.html", {'fbooks': fictionBook})
