from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy


class UserAlreadyLoggedIn:
    redirect_url = reverse_lazy("chats:home")

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)
        return super(UserAlreadyLoggedIn, self).dispatch(request, *args, **kwargs)
