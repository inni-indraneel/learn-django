from django.db import models

# Create your models here.
class employee(models.Model):
  first_name = models.CharField(max_length = 30)
  last_name = models.CharField(max_length = 30)
  sal = models.CharField(max_length = 30, blank = True)

  def __str__(self):
    return (f"name : {self.first_name} {self.last_name} \n salary: {self.sal}")

