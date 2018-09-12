from django.shortcuts import render
from django.http import HttpResponse


posts = [
  {
    'author':"Thomas",
    'title':"Blog post 1",
    'content':'first post content',
    'date_posted':'august 27, 2018'
  },
  {
    'author':"John",
    'title':"Blog post 2",
    'content':'second post content',
    'date_posted':'august 30, 2018'
  }
]



def home(request):
  # return HttpResponse("<h1> blog home </h1>")

  obj = {
    "posts":posts
  }
  return render(request,'blog/home.html', obj) ## django knows templates folder ny default


def about(request):
  # return HttpResponse("<h1> blog about </h1>")
  return render(request,'blog/about.html', {'title':"About"})
