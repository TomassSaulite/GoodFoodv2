from django import forms

class CustomAuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
