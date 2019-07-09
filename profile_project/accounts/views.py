from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from . import forms
from . import models


def retrieve_profile(request, pk):
    """This function retrieves the profile from the user."""
    user = get_object_or_404(models.User, pk=pk)
    profile = get_object_or_404(models.Profile, user=user)
    return profile


def sign_in(request):
    """View to let the user sign in."""
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse('home')
                    )
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    """View to let a user create an account and then signs them in."""
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return HttpResponseRedirect(reverse('accounts:create_profile'))
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_out(request):
    """View that signs the user out."""
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))


def create_profile(request):
    """View that lets the user create a profile."""
    form = forms.ProfileForm()

    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Profile added!')
            return HttpResponseRedirect(reverse('accounts:view_profile',
                                                kwargs={'pk': request.user.pk}))
    return render(request, 'accounts/profile_form.html', {'form': form})


def view_profile(request, pk):
    """View to let the user view the full details of there profile."""
    profile = retrieve_profile(request, pk)
    return render(request, 'accounts/view_profile.html', {'profile': profile})


def edit_profile(request, pk):
    """View that allows the user to edit there profile."""
    profile = retrieve_profile(request, pk)
    form = forms.ProfileForm(instance=profile)

    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated profile successfully!')
            return HttpResponseRedirect(profile.get_absolute_url())
    return render(request, 'accounts/profile_form.html', {'form': form})


def edit_password(request, pk):
    """View that lets the user edit there password."""
    user = get_object_or_404(models.User, pk=pk)
    form = PasswordChangeForm(user)

    if request.method == 'POST':
        form = PasswordChangeForm(user, data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=user.username,
                password=form.cleaned_data['new_password1']
            )
            login(request, user)
            messages.success(
                request,
                "Password has been changed successfully."
            )
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'accounts/edit_password.html', {'form': form})
