from django.shortcuts import render
from django.views import View
from .forms import CustomAuthenticationForm
from .forms import UserRegistrationForm



class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
class Login(View):
    def get(self, request, *args, **kwargs):
        form_class = CustomAuthenticationForm
        return render(request, 'login.html')
    
class Register(View):
    def get(self, request, *args, **kwargs):
        form_class = UserRegistrationForm
        return render(request, 'register.html')
     
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

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

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            print(username)
            print(password)
            if user is not None:
                login(request, user)
                # updateLastAccess()
                return redirect('index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

