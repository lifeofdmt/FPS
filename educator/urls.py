from django.urls import path
from . import views

app_name = "educator"
urlpatterns = [
    path("", views.index, name="index"),
    path("records", views.records, name="records"),
    path("logout", views.logout, name="logout"),
    path("profile", views.profile, name="profile"),
    path("settings", views.settings, name="settings"),
    path("enroll", views.enroll, name="enroll"),
    path("report", views.report, name="report"),
    path("grading", views.grading, name="grading")
]