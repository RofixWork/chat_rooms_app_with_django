from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView

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
        return redirect(reverse("chats:chat_room", kwargs={"slug": room.slug}))

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
        try:
            return ChatRoom.objects.get(slug=slug)
        except ChatRoom.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        if not self.get_object():
            messages.error(request, "Room not found.")
            return redirect(reverse("chats:home"))
        return super().get(request, *args, **kwargs)


class DeleteChatRoomView(LoginRequiredMixin, DeleteView):
    model = ChatRoom
    success_url = reverse_lazy("chats:home")

    def form_valid(self, form):
        messages.success(self.request, "Room deleted successfully.")
        return super().form_valid(form)

    def get_object(self, queryset=None):
        room_slug = self.kwargs.get("slug")
        user = self.request.user
        return get_object_or_404(ChatRoom, slug=room_slug, user=user)


home_view = HomePageView.as_view()
create_new_room_view = CreateNewRoomView.as_view()
chat_room_view = ChatRoomView.as_view()
delete_chat_room_view = DeleteChatRoomView.as_view()
