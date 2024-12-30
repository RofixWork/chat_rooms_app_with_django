from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView

from .forms import CreateRoomForm
from .models import ChatMessage, ChatRoom


# HomePageView handles the display of all chat rooms and the room creation form
class HomePageView(LoginRequiredMixin, ListView):
    template_name = "chats/home.html"  # Template for the homepage
    model = ChatRoom  # Model representing the chat rooms
    context_object_name = "rooms"  # Context variable name for the chat rooms

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        # Add extra context to the template
        context = super().get_context_data(**kwargs)
        context["form_create_room"] = CreateRoomForm()  # Form for creating a new room
        return context


# CreateNewRoomView handles the creation of new chat rooms
class CreateNewRoomView(LoginRequiredMixin, CreateView):
    model = ChatRoom  # Model representing the chat rooms
    form_class = CreateRoomForm  # Form for creating a new chat room

    def form_valid(self, form):
        # Save the room and associate it with the logged-in user
        room = form.save(commit=False)
        room.user = self.request.user
        room.save()
        # Redirect to the new chat room
        return redirect(reverse("chats:chat_room", kwargs={"slug": room.slug}))

    def form_invalid(self, form):
        # Handle the case where the room name already exists
        messages.error(self.request, "Already exist room name.")
        return redirect(reverse("chats:home"))


# ChatRoomView displays the details of a specific chat room
class ChatRoomView(LoginRequiredMixin, DetailView):
    model = ChatRoom  # Model representing the chat rooms
    template_name = "chats/chat-room.html"  # Template for the chat room
    context_object_name = "room"  # Context variable name for the chat room

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        # Add extra context to the template
        context = super().get_context_data(**kwargs)
        context["rooms"] = ChatRoom.objects.all()  # All chat rooms
        context["form_create_room"] = CreateRoomForm()  # Room creation form
        context["room_messages"] = ChatMessage.objects.filter(
            room=self.get_object()
        )  # Messages in the current room
        return context

    def get_object(self, queryset=None):
        # Retrieve the chat room based on the slug
        slug = self.kwargs.get("slug")
        try:
            return ChatRoom.objects.get(slug=slug)
        except ChatRoom.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        # Handle the case where the room does not exist
        if not self.get_object():
            messages.error(request, "Room not found.")
            return redirect(reverse("chats:home"))
        return super().get(request, *args, **kwargs)


# DeleteChatRoomView handles the deletion of a specific chat room
class DeleteChatRoomView(LoginRequiredMixin, DeleteView):
    model = ChatRoom  # Model representing the chat rooms
    success_url = reverse_lazy("chats:home")  # URL to redirect after deletion

    def form_valid(self, form):
        # Add a success message after deleting the room
        messages.success(self.request, "Room deleted successfully.")
        return super().form_valid(form)

    def get_object(self, queryset=None):
        # Retrieve the chat room to delete based on the slug and user
        room_slug = self.kwargs.get("slug")
        user = self.request.user
        return get_object_or_404(ChatRoom, slug=room_slug, user=user)


# Function-based views for easier URL routing
home_view = HomePageView.as_view()
create_new_room_view = CreateNewRoomView.as_view()
chat_room_view = ChatRoomView.as_view()
delete_chat_room_view = DeleteChatRoomView.as_view()
