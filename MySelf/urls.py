from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.home, name="about"),
    path("contact/", views.contact, name="contact"),
    path("skills/", views.skills, name="skills"),
    path("education/", views.education, name="education"),
    
]