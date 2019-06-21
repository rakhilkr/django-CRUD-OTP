from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class testform(forms.ModelForm):
    class Meta:
        model = log
        fields = '__all__'


class Testform(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'


class loginform(forms.ModelForm):
    class Meta():
        model = log
        fields = ['User','Password','Password2','Name','Email','Phone']


