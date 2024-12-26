from django.urls import path

from . import views

urlpatterns = [path("sign-in", views.register_view, name="register")]
