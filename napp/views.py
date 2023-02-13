from django.shortcuts import render
from .models import Notes
# Create your views here.
def list(request):
    all_notes =Notes.objects.all()
    return render(request,'napp/listp.html',{'notes':all_notes})