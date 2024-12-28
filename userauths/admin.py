from django.contrib import admin

from .models import Profile, User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_staff", "is_superuser")
    search_fields = ("id", "username", "email")
    list_filter = ("is_staff", "is_superuser")
    ordering = ("-id",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "thumbnail", "created_at", "updated_at")
    search_fields = ("id", "user__username")
    ordering = ("-id",)
