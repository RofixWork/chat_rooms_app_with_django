from django.contrib import admin

from .models import ChatMessage, ChatRoom


# Register your models here.
@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "created_at")
    search_fields = ("id", "name", "slug")
    ordering = ("-id",)


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("id", "room", "user", "message", "created_at")
    search_fields = ("id", "room", "user", "message")
    ordering = ("-id",)
