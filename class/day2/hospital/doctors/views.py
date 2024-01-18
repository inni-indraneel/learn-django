from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest
# Create your views here.
def get_name(request):
    return HttpResponse("Hello name")