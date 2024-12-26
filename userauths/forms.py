from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import User

class_value = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": class_value, "placeholder": "**********"}
        ),
        label="Your Password",
        
        
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": class_value, "placeholder": "**********"}
        ),
        label="Confirm Password",
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(
                attrs={"class": class_value, "placeholder": "jhon doe"}
            ),
            "email": forms.EmailInput(
                attrs={"class": class_value, "placeholder": "jhondoe@gmail"}
            ),
        }
        labels = {
            "username": "Username",
            "email": "Your Email",
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError(
                "Oops! The passwords don’t match. Please double-check and try again. 😊"
            )

        return password2


class SignInForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": class_value, "placeholder": "jhondoe@gmail"}
        ),
        label="Email",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": class_value, "placeholder": "**********"}
        ),
        label="Password",
    )
