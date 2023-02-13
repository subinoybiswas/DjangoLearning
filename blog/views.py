from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'blog/home.html')
@login_required
def auth(request):
    return render(request,'blog/auth.html')