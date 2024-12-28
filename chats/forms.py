from django import forms

from .models import ChatRoom

input_class = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": input_class, "placeholder": "Room Name"}
            ),
        }
