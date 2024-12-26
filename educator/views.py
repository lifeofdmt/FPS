from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def logout(request):
    pass

def index(request):
    return render(request, "teacher/index.html")

def profile(request):
    pass

def records(request):
    return render(request, "teacher/records.html")

def settings(request):
    pass

def enroll(request):
    pass

def report(request):
    pass

def grading(request):
    pass
