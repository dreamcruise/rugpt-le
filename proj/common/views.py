from django.shortcuts import render, redirect
from .models import Request

# Create your views here.
def home(request):
    if request.method == 'POST':
        pass
    return render(request, 'common/home.html')

def tariffs(request):
    return render(request, 'common/tariffs.html')

def contacts(request):
    return render(request, 'common/contacts.html')

def methods_description(request):
    #if request.user.is_authenticated:
    return render(request, 'common/methods.html')
    #return redirect('home')