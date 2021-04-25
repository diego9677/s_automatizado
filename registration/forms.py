from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'w-full px-2 text-sm py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-600'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-2 text-sm py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-600'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-2 text-sm py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-600'
    }))

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-2 text-sm py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-600'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-2 text-sm py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-600'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-2 text-sm py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-600'
            }),
        }