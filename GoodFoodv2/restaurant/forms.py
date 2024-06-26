from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomRestAuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


from django.contrib.auth.forms import UserCreationForm
from .models import customRest

class RestRegistrationForm(UserCreationForm): 
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
        help_text=None,
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        strip=False,
        help_text=None,
    )   
    name = forms.CharField(max_length=30, required=True, help_text=None)
    email = forms.EmailField(max_length=254, required=True, help_text=None)
    country = forms.CharField(max_length=3, required=True)
    city = forms.CharField(max_length=3, required=True)
    class Meta(UserCreationForm.Meta):
        model = customRest
        fields =UserCreationForm.Meta.fields+('name',  'email', 'country','city',)
