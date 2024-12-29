from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "auth"

urlpatterns = [
    path("sign-up/", views.register_view, name="register"),
    path("sign-in/", views.login_view, name="login"),
    path("sign-out/", LogoutView.as_view(), name="logout"),
    path("profile/edit", views.edit_profile_view, name="edit_profile"),
]
