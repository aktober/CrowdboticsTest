from django import forms
from django.contrib.auth.models import User
from app import models


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class OwnerForm(forms.ModelForm):
    class Meta:
        model = models.Owner
        fields = ('name',)