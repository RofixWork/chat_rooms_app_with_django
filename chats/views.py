from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from .forms import CreateRoomForm
from .models import ChatMessage, ChatRoom


# Create your views here.
class HomePageView(LoginRequiredMixin, ListView):
    template_name = "chats/home.html"
    model = ChatRoom
    context_object_name = "rooms"

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

    def form_invalid(self, form):
        messages.error(self.request, "Already exist room name.")
        return redirect(reverse("chats:home"))


class ChatRoomView(LoginRequiredMixin, DetailView):
    model = ChatRoom
    template_name = "chats/chat-room.html"
    context_object_name = "room"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["rooms"] = ChatRoom.objects.all()
        context["form_create_room"] = CreateRoomForm()
        context["room_messages"] = ChatMessage.objects.filter(
            room=self.get_object()
        ).order_by("created_at")
        return context

    def get_object(self, queryset=None):
        slug = self.kwargs.get("slug")
        return get_object_or_404(ChatRoom, slug=slug)


home_view = HomePageView.as_view()
create_new_room_view = CreateNewRoomView.as_view()
chat_room_view = ChatRoomView.as_view()
