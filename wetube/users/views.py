import logging
from math import e
from smtplib import SMTPException

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Profile, User
from .forms import UserForm, UserUpdateForm
from posts.models import Posts
from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import EmailMessage

log = logging.getLogger(__name__)


def registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]

            messages.success(request, f"Welcome to wetube {username}!")
            form.save(commit=True)

            try:
                send_mail(
                    "Success!",
                    f"account {username} successfully created",
                    settings.EMAIL_HOST_USER,
                    ["shaxruz2905@gmail.com"],
                    fail_silently=False,
                )
            except SMTPException as error:
                print("--------------------------------------------")
                print("Error while sending email: ", error)
                print("--------------------------------------------")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
            context = {"form": form}
            return render(request, "registration/create_user.html", context)

    context = {"form": UserForm()}
    return render(request, "registration/create_user.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            user = u_form.save(commit=True)

            messages.success(request, f"Your account has been updated!")
            return redirect("profile")
        else:
            context = {
                "u_form": u_form,
                "posts": Posts.objects.filter(author=request.user),
            }
            return render(request, "profile.html", context)

    context = {
        "u_form": UserUpdateForm(instance=request.user),
        "posts": Posts.objects.filter(author=request.user),
    }
    return render(request, "profile.html", context)
