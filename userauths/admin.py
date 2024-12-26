from django.contrib import admin

from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_staff", "is_superuser")
    search_fields = ("id", "username", "email")
    list_filter = ("is_staff", "is_superuser")
    ordering = ("-id",)
