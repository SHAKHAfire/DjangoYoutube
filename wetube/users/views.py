import logging
from math import e

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Profile
from .forms import UserForm, UserUpdateForm


log = logging.getLogger(__name__)


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to wetube {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/create_user.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/create_user.html', context)


@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            user = u_form.save(commit=True)

            messages.success(request,
                             f"Your account has been updated!")
            return redirect('profile')
        else:
            context = {
                "u_form": u_form,

            }
            return render(request, 'profile.html', context)

    context = {
        'u_form': UserUpdateForm(instance=request.user),

    }
    return render(request, 'profile.html', context)

def all_users(request):
    users=Profile.objects.all()
    context={'users':users}
    return render(request,'all_users.html',context)