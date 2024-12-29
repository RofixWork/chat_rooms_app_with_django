from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView

from utils.mixins import UserAlreadyLoggedIn

from .forms import EditProfileForm, SignInForm, SignUpForm
from .models import Profile, User


# Create your views here.
class RegisterView(UserAlreadyLoggedIn, CreateView):
    model = User
    template_name = "userauths/sign-up.html"
    form_class = SignUpForm

    def form_valid(self, form: SignInForm):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")

        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)
            return redirect("/")
        else:
            form.add_error(None, "Invalid Credentials")
            return self.form_invalid(form)


class LoginView(UserAlreadyLoggedIn, FormView):
    template_name = "userauths/sign-in.html"
    form_class = SignInForm
    success_url = "/"

    def form_valid(self, form: SignInForm):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)
            return redirect("/")
        else:
            form.add_error(None, "Invalid Credentials")
            return self.form_invalid(form)


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = "userauths/edit-profile.html"
    success_url = reverse_lazy("auth:edit_profile")

    def form_valid(self, form):
        messages.success(self.request, "Profile updated successfully.")
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user.profile


register_view = RegisterView.as_view()
login_view = LoginView.as_view()
edit_profile_view = EditProfileView.as_view()
