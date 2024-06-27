from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.views import View
from .forms import CustomUserAuthenticationForm, UserRegistrationForm
from django.contrib import messages

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
class Empty(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'empty.html')
    
class UserLogin(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserAuthenticationForm()
        return render(request, 'userLogin.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = CustomUserAuthenticationForm()
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                print("!!!!!!!!!!!")
                return redirect('userRegister')
            else:
                messages.error(request, 'Invalid email or password.')
                
        # return render(request, 'empty.html', {'form': form})
        return redirect('userRegister')
    
class UserRegister(View):
    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        return render(request, 'userRegister.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
        return render(request, 'userRegister.html', {'form': form})

