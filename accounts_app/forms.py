from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    full_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('full_name','username', 'email', 'password1' ,'password2' )