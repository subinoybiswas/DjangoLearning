from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ok(request):
    return HttpResponse('<h1>HELLO</h1>')
def abbc(request):
    return render(request,'newapp/abcd.html')