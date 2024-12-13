from django.shortcuts import render
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