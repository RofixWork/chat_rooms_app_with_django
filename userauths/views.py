from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic.edit import CreateView

from .forms import SignInForm
from .models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    template_name = "userauths/sign-in.html"
    form_class = SignInForm

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


register_view = RegisterView.as_view()
