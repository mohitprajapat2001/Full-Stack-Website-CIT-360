from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("accounts", views.accounts, name="Accounts"),
    path("register", views.register, name="Accounts"),
    path("login", views.login, name="Accounts"),
    path("logout", views.logout, name="Accounts"),
]
