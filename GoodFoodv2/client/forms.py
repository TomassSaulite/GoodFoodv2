from django import forms
from django.contrib.auth.forms import UserCreationForm
class CustomAuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")




from django.contrib.auth.forms import UserCreationForm
from .models import customUser

class UserRegistrationForm(UserCreationForm):    
    username = forms.CharField(label="Username",help_text=None)
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    country = forms.CharField(max_length=3, required=True)
    class Meta(UserCreationForm.Meta):
        model = customUser
        fields =UserCreationForm.Meta.fields+('first_name', 'last_name', 'email', 'country')
    USERNAME_FIELD = 'email'
