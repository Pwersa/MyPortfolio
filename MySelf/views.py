from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'html_files/about.html')

def contact(request):
    return render(request, 'html_files/contact.html')

def skills(request):
    return render(request, 'html_files/skills.html')