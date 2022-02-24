from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base/index.html')

def hostels(request):
    return render(request, 'base/hostels.html')

def users(request):
    return render(request, 'base/users.html')

def contact(request):
    return render(request, 'base/contact.html')

def about(request):
    return render(request, 'base/about.html')

