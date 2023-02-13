from django.shortcuts import render
from .models import Notes
from django.http import Http404
# Create your views here.
def list(request):
    all_notes =Notes.objects.all()
    return render(request,'napp/listp.html',{'notes':all_notes})
def detail(request,tk):
    try:
        notee = Notes.objects.get(pk=tk)
    except Notes.DoesNotExist:
        raise Http404
    return render(request,'napp/detail.html',{'note':notee})