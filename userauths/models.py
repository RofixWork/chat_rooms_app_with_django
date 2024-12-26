from django.contrib.auth.models import AbstractUser
from django.db import models


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
