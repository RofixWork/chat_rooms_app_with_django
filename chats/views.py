from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, TemplateView

from .forms import CreateRoomForm
from .models import ChatRoom

# Create your views here.


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "chats/home.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form_create_room"] = CreateRoomForm()
        return context
class CreateNewRoomView(LoginRequiredMixin, CreateView):
    model = ChatRoom
    form_class = CreateRoomForm

    def form_valid(self, form):
        room = form.save(commit=False)
        room.user = self.request.user
        room.save()
        return redirect(reverse("chats:home"))


home_view = HomePageView.as_view()
create_new_room_view = CreateNewRoomView.as_view()
