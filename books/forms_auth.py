from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

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

class BootstrapUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "autocomplete": "email",
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "autocomplete": "username",
        "autocapitalize": "none",
    }))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "autocomplete": "new-password",
    }))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "autocomplete": "new-password",
    }))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get("email", "")
        if commit:
            user.save()
        return user
