from django.shortcuts import render, redirect
from .models import StudentDAO


# Create your views here.

dao = StudentDAO()

def index(request):
    return render(request, 'index.html')

def submit(request):
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        dob = request.POST['dob']
        print(first_name, last_name, dob)
        student = dao.add_student_by_name(f_name=first_name, l_name=last_name, dob=dob)

        student.save()

    return redirect('view_data')

def view_data(request):
    student_data = dao.get_all_student()
    return render(request, 'output.html', {'data': student_data})
