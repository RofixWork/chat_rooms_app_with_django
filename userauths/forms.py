from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class_value = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"


class SignInForm(UserCreationForm):
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
