from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hellow_world(request):
    return HttpResponse( "Hellow World" )

def home_page(request):
    return render(request , "index.html")

def task_page(request):
    task_data='HURRAY! Task Completed'
    return render(request , "task.html",{'task_data':task_data})