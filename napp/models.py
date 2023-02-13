from django.db import models

# Create your models here.
class Notes(models.Model):
    titile = models.CharField(max_length=256)
    text =models.TextField()
    dete= models.DateTimeField(auto_now_add=True)