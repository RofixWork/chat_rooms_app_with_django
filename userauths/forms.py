from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Profile, User

class_value = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
edit_form_input_class = "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"


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


class EditProfileForm(forms.ModelForm):

    image = forms.ImageField(
        widget=forms.widgets.ClearableFileInput(
            attrs={
                "class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400",
                "placeholder": "Upload a profile picture",
                "accept": "image/*",
            }
        )
    )

    class Meta:
        model = Profile
        fields = ("image", "first_name", "last_name", "phone", "city", "country", "bio")
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": edit_form_input_class, "placeholder": "John Doe"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": edit_form_input_class, "placeholder": "Doe"}
            ),
            "phone": forms.TextInput(
                attrs={"class": edit_form_input_class, "placeholder": "+1 123 456 7890"}
            ),
            "city": forms.TextInput(
                attrs={"class": edit_form_input_class, "placeholder": "New York"}
            ),
            "country": forms.TextInput(
                attrs={"class": edit_form_input_class, "placeholder": "USA"}
            ),
            "bio": forms.Textarea(
                attrs={
                    "class": edit_form_input_class,
                    "placeholder": "Write a brief bio...",
                }
            ),
        }
