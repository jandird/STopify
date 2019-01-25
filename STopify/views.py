
from django.shortcuts import render


def stopify(request):
    return render(request, 'stopify.html')


def callback(request):
    return render(request, 'loginFinish.html', {})


def home(request):
    return render(request, 'home.html')