from . import views
from django.urls import path
urlpatterns = [
    path("", views.addition),
    path("student_surname/", views.get_surname),
    path("student_roll/", views.get_Roll),
]
