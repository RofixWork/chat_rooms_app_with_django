from django.urls import path

from . import views

app_name = "auth"

urlpatterns = [
    path("sign-up/", views.register_view, name="register"),
    path("sign-in/", views.login_view, name="login"),
]
