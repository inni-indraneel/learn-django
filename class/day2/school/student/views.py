from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def addition(request: HttpRequest):
     if request.method == "POST": 
         num1 = request.POST.get('num1', 0)
         num2 = request.POST.get('num2', 0)
         res = int(num1) + int(num2)
         return HttpResponse(f"Result is {res}")
     else:
         return render(request, "addition.html")





def get_surname(name):
    return HttpResponse("Hello surname")

def get_Roll(req):
    return render(req, "test.html")

def get_Marks(req):
    return render(req, "test.html")
