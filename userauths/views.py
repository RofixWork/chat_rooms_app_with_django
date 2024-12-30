from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView

from utils.mixins import UserAlreadyLoggedIn

from .forms import EditProfileForm, SignInForm, SignUpForm
from .models import Profile, User


# Class-based view to handle user registration
class RegisterView(UserAlreadyLoggedIn, CreateView):
    model = User  # The User model to save new users
    template_name = "userauths/sign-up.html"  # Template for the registration page
    form_class = SignUpForm  # Form class for registration

    def form_valid(self, form: SignInForm):
        # Save the form data to create a new user
        form.save()
        email = form.cleaned_data.get("email")  # Get the email from the form
        password = form.cleaned_data.get("password1")  # Get the password from the form

        # Authenticate the newly registered user
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            # Log the user in and redirect to the home page
            login(self.request, user)
            return redirect("/")
        else:
            # Add an error if authentication fails
            form.add_error(None, "Invalid Credentials")
            return self.form_invalid(form)


# Class-based view to handle user login
class LoginView(UserAlreadyLoggedIn, FormView):
    template_name = "userauths/sign-in.html"  # Template for the login page
    form_class = SignInForm  # Form class for login
    success_url = "/"  # URL to redirect after successful login

    def form_valid(self, form: SignInForm):
        email = form.cleaned_data.get("email")  # Get the email from the form
        password = form.cleaned_data.get("password")  # Get the password from the form

        # Authenticate the user
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            # Log the user in and redirect to the home page
            login(self.request, user)
            return redirect("/")
        else:
            # Add an error if authentication fails
            form.add_error(None, "Invalid Credentials")
            return self.form_invalid(form)


# Class-based view to handle profile editing
class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile  # The Profile model to update user profiles
    form_class = EditProfileForm  # Form class for editing profiles
    template_name = "userauths/edit-profile.html"  # Template for the profile edit page
    success_url = reverse_lazy(
        "auth:edit_profile"
    )  # URL to redirect after successful profile update

    def form_valid(self, form):
        # Add a success message after the profile is updated
        messages.success(self.request, "Profile updated successfully.")
        return super().form_valid(form)

    def get_object(self, queryset=None):
        # Retrieve the profile of the currently logged-in user
        return self.request.user.profile


# Function-based views for easier URL routing
register_view = RegisterView.as_view()
login_view = LoginView.as_view()
edit_profile_view = EditProfileView.as_view()
