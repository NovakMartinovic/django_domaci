from django.contrib.auth.models import User
from django import forms
from .models import Poruka

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

class SearchForm(forms.ModelForm):
    class Meta:
        model = Poruka
        fields = ['title']
