from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import UserRegisterForm

def register(request):
    print('request.POST==>',request.POST)
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
    "form":form
    }
    return render(request,'users/register.html',obj)


def profile(request):
       return render(request, 'users/profile.html' )