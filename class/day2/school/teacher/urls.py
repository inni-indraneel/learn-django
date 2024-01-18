from . import views
from django.urls import path
urlpatterns = [
    path("teacher_name/", views.get_name),
    path("teacher_surname/", views.get_surname),
    path("teacher_id/", views.get_id),
]
