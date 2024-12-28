from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "chats/home.html"


home_view = HomePageView.as_view()
