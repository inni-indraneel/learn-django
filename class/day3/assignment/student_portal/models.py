from django.db import models

# Create your models here.
class Student(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    dob = models.DateField()
    
    
    def __str__(self):
        return f"Name -> {self.f_name} {self.l_name}"
    

class StudentDAO():

    def get_all_student(self):
        return Student.objects.all()
    
    def get_student_by_id(self, id):
        return Student.objects.get(id=id)
    
    def update_student(self, student):
        student.save()
        return student
    
    def delete_student(self, id):
        student = Student.objects.get(id=id)
        student.delete()
        return student    
    
    def add_student_by_name(self, f_name, l_name, dob):
        student = Student(f_name=f_name, l_name=l_name, dob=dob)
        student.save()
        return student        