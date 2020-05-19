from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'input100',
    }))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'input100'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input100'
    }))
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'class': 'input100'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100'
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
