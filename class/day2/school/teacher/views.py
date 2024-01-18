from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_name(name):
    return HttpResponse("Hello Name")

def get_surname(name):
    return HttpResponse("Hello surname")

def get_id(name):
    return HttpResponse("Hello Id")
