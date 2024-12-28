from django.contrib import admin

from .models import ChatRoom


# Register your models here.
@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "created_at")
    search_fields = ("id", "name", "slug")
    ordering = ("-id",)
