from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "first_name", "last_name", "age"]
        error_messages = {
            "username": {"unique": "Username is Already Exists."},
            "email": {"unique": "Email is Already Exists."},
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "first_name", "last_name", "age"]
