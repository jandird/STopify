from django.http import HttpResponse
from django.shortcuts import render

def stopify(request):
    # return HttpResponse("STopify")
    return render(request, 'stopify.html')
