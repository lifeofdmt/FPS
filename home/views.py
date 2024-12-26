from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django import forms
from . import sform
import pandas as pd


# Create your views here.
def index(request):
    return render(request, "unlogged/index.html")

def enroll(request):
    #country_file = pd.read_csv('countryInfo.txt', delimiter='\t')
    return render(request, "unlogged/enroll.html")

def about(request):
    return render(request, "unlogged/about.html")

def register(request):
    if request.method == "POST":
        form = forms.Form(request.POST)
        if form.is_valid():
            return render(request, "unlogged/register2.html")
        else:
            return HttpResponse("bad")
    form = sform.register1_form()        
    return render(request, "unlogged/register1.html", {
        "form": form
    })

def login(request):
    return render(request, 'unlogged/login.html')
