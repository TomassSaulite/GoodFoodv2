from django.shortcuts import render
from django.views import View
from .forms import CustomAuthenticationForm



class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    
class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')
     
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomAuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})
