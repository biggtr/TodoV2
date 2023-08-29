from django.urls import path, include
from .views import SignupView

urlpatterns = [
    path("signup/", SignupView, name="signup"),
    path("", include("django.contrib.auth.urls")),
]
