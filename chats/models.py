from autoslug import AutoSlugField
from django.db import models


# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from="name", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Chat Room"
        verbose_name_plural = "Chat Rooms"

    def __str__(self):
        return self.name
