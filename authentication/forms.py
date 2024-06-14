from django import forms
from .models import Project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=40,label="Username",widget=forms.TextInput(attrs={
        'placeholder':'username',
        'autocomplete':'off'
        }))

    password1 = forms.CharField(max_length=40,label='Password',widget=forms.TextInput(attrs={
        'placeholder':'password',
        'autocomplete':'off',
        'type':'password',
    }))

    password2 = forms.CharField(max_length=40,label='Password Again',widget=forms.TextInput(attrs={
        'placeholder':'password',
        'autocomplete':'off',
        'type':'password',
    }))

    class Meta:
        model = User
        fields = ('username','password1','password2')


