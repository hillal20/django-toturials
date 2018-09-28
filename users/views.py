from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    print('request.POST==>', request.POST)
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        print('form==>', form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(f'username ===> {username}')
            messages.success(request, f'=== Account created for {username} ====')
            return redirect('login')
    else:
        form = UserRegisterForm()

    obj = {
        "form": form
    }
    return render(request, 'users/register.html', obj)


@login_required
def profile(request):
    if request.method == "POST":
        uForm = UserUpdateForm(request.POST, instance=request.user)
        pForm = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if uForm.is_valid() and pForm.is_valid():
            uForm.save()
            pForm.save()
            messages.success(request, f'=== Account is Updated !!!!  ====')
            return redirect('profile')
    else:
        uForm = UserUpdateForm(instance=request.user)
        pForm = ProfileUpdateForm(instance=request.user.profile)
    obj = {
        'uForm': uForm,
        'pForm': pForm
    }
    return render(request, 'users/profile.html', obj)
