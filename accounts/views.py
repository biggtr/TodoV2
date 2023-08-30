from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.urls import reverse_lazy
from accounts.models import CustomUser
from .forms import CustomUserCreationForm

# Create your views here.


def SignupView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task-list")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", context={"form": form})
