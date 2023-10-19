from .models import Users
from django.forms import ModelForm, TextInput


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'phone']

        widgets = {
            'name': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Username"
                }),
            'phone': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone number"
                })
        }