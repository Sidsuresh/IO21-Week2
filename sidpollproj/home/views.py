from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, "index.html", {})

def contact(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about(request, *args, **kwargs):
    return render(request, "aboutme.html", {})