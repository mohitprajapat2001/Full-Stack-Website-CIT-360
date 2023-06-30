from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("gallery/<category>", views.gallery, name="Home"),
    path("profile/<username>", views.profile, name="Student Panel"),
    path("edituser/<username>", views.edituser, name="Edit Student"),
    path("facultyedit/<username>", views.facultyedit, name="Edit Faculty Data"),
    path("panel/<role>", views.panel, name="Panel"),
    path("notesdownload", views.notesdownload, name="Notes Download"),
    path("documentview/<document>", views.documentview, name="Notes Download"),
    path("achievements", views.achievements, name="Notes Download"),
    path("notescreate", views.notescreate, name="Note Create"),
    path("internshipcreate", views.internshipcreate, name="Internship Create"),
    path("seminarcreate", views.seminarcreate, name="Seminar Create"),
    path("internship/<data>", views.internshipdetails, name="Seminar Create"),
]
