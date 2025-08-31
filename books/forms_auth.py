from django import forms
from django.contrib.auth.forms import AuthenticationForm

class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control",
            "autocomplete": "username",
            "autocapitalize": "none",
            "autofocus": True,})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control",
            "autocomplete": "current-password",})
    )