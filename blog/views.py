from django.shortcuts import render
from django.http import HttpResponse
from .models import Post





def home(request):
  # return HttpResponse("<h1> blog home </h1>")

  obj = {
    "posts":Post.objects.all()
  }
  return render(request,'blog/home.html', obj) ## django knows templates folder ny default


def about(request):
  # return HttpResponse("<h1> blog about </h1>")
  return render(request,'blog/about.html', {'title':"About"})
