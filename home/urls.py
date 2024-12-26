from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("enroll", views.enroll, name="enroll"),
    path("about", views.about, name="about"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login")
]