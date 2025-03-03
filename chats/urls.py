from django.urls import path

from . import views

app_name = "chats"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("create-room/", views.create_new_room_view, name="create_room"),
    path("room/<slug:slug>/", views.chat_room_view, name="chat_room"),
    path(
        "delet-room/<slug:slug>/delete/",
        views.delete_chat_room_view,
        name="delete_chat_room",
    ),
]
