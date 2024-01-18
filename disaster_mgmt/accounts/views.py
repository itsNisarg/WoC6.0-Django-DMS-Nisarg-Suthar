from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')


def contact(request):
    return render(request, 'accounts/contact.html')


def about(request):
    return render(request, 'accounts/about.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
