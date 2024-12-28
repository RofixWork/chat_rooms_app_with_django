from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def save(self, *args, **kwargs):
        if not self.username:
            email_username = self.email.split("@")[0]
            self.username = email_username.strip().lower()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="profile_pics",
        default="profile_pics/default.png",
        validators=[
            validators.FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])
        ],
    )
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def thumbnail(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.image.url}" width="40" height="40" style="border-radius: 5px;">'
            )
        return "No Image"

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"
        ordering = ["-created_at"]

    def __str__(self):
        return self.user.username
