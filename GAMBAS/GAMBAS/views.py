from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# import render
# Create your views here.

def index(response):
    return render(response, "GAMBAS/index.html", {})


