from django.shortcuts import render

# Create your views here.


def showmain(request):
    return render(request, 'main/mainpage.html')


def intro(request):
    return render(request, 'main/intro.html')