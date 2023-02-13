from django.shortcuts import render
from django.http import HttpResponse
def abc(request):
    return HttpResponse('<h1>Hi</h1>')
