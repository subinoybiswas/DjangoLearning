from django.shortcuts import render
from .models import Notes
# Create your views here.
def list(request):
    all_notes =Notes.objects.all()
    return render(request,'napp/listp.html',{'notes':all_notes})
def detail(request,tk):
    notee = Notes.objects.get(pk=tk)
    return render(request,'napp/detail.html',{'note':notee})