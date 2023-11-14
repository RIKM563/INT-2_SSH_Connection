from .models import Input, Information
from django import forms
from django.forms import ModelForm, TextInput


class InfoForm(ModelForm):
    class Meta:
        model = Input
        fields = ["hostname", "username", "password", "port"]
        widgets = {
            "hostname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'hostname'
            }),
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }),
            "port": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'port'
            })
            }


class NewForm(ModelForm):
    model = Information
    fields = ["OS", "info"]
