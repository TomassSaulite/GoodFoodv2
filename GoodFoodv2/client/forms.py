from django import forms
from django.contrib.auth.forms import UserCreationForm



class CustomAuthenticationForm(forms.Form):
    # email = forms.CharField(widget=forms.CharField( label="Email"))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}), label="Email")
    # username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


from django.contrib.auth.forms import UserCreationForm
from .models import customUser

class UserRegistrationForm(UserCreationForm): 
    # username = forms.CharField(
    #     label="Username",
    #     help_text=None,
    # )
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
    # username = forms.CharField(label="Username",help_text=None)
    first_name = forms.CharField(max_length=30, required=True, help_text=None)
    last_name = forms.CharField(max_length=30, required=True, help_text=None)
    email = forms.EmailField(max_length=254, required=True, help_text=None)
    country = forms.CharField(max_length=3, required=True)
    class Meta(UserCreationForm.Meta):
        model = customUser
        fields =UserCreationForm.Meta.fields+('first_name', 'last_name', 'email', 'country')
        # fields =('first_name', 'last_name', 'email', 'country')
