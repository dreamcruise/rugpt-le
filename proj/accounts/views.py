from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404, HttpResponseForbidden

from .forms import UserAccountCreationForm, CustomAuthenticationForm
from .models import PrivateKey, UserAccount
from .utils import create_key, send_created_key

# Create your views here.

class UserCreation(CreateView):
    form_class = UserAccountCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/registration.html'

class CustomLogin(LoginView):
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'

'''class PrivateKeyDeletion(DeleteView):
    model = PrivateKey
    template_name = 'account/pk_detail.html'
    success_url = reverse_lazy('dashboard')
'''

def show_pk(request, user_slug, pk_slug):
    pk = PrivateKey.objects.get(pk_slug=pk_slug)
    context={'pk': pk}
    return render(request, 'accounts/pk_detail.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def dash(request, user_slug):
    if request.user.is_authenticated and request.user.username == user_slug:
        context = {}
        user = UserAccount.objects.get(username=request.user.username)
        if request.method == 'POST':
            private_key = PrivateKey.objects.create(
                key = create_key(), 
                status = "activated",
                user = user
            )

            send_created_key(private_key.key)
            private_key.save()
            
        if PrivateKey.objects.filter(user=user).exists:
            keys = PrivateKey.objects.filter(user=user)
            context['keys'] = keys
        return render(request, 'accounts/dashboard.html', context=context)
    return redirect('home')

def show_balance(request, user_slug):
    return render(request, 'accounts/balance.html')

def save_payment(request):
    if request.method == 'POST':
        #key, model, data
        return HttpResponse()
    return redirect('home')

@csrf_exempt
def check_key(request):
    if request.method == 'POST':
        autorization = request.headers.get('Authorization', '')

        parts = autorization.split(' ')
        
        if len(parts) != 2 or parts[0] != 'Bearer':
            return HttpResponseForbidden('Invalid key was provied!')
        if PrivateKey.objects.filter(key=parts[1]).exists():
            return HttpResponse(status=200)
        return HttpResponseForbidden('The key was not found!')
    
    return Http404('The page is not found!')