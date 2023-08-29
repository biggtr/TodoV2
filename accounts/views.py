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
            email = form.cleaned_data["email"]
            if CustomUser.objects.filter(email=email).exists():
                form.add_error("email", "This email address is already registered.")

            else:
                user = form.save()
                login(request, user)
                return redirect(reverse_lazy("task_list"))
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", context={"form": form})
