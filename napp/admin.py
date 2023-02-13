from django.contrib import admin
from . import models
# Register your models here.
class okABC(admin.ModelAdmin):
    list_display = ('titile',)
    

admin.site.register(models.Notes,okABC)