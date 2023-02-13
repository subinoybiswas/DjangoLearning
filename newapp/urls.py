from django.urls import path
from . import views
urlpatterns = [
    path('', views.ok,name ="OK"),
    path('abcd/',views.abbc,name="abbc"),
]
    