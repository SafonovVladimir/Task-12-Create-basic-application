from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return render(request, 'index.html')


def profile(request, user_name):
    return render(request, 'profile.html', {'name': user_name})


def tests(request):
    return HttpResponse("<h1>TESTS</h>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>PAGE NOT FOUND!</h>")
