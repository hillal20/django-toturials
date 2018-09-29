from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView


def home(request):
    # return HttpResponse("<h1> blog home </h1>")

    obj = {
        "posts": Post.objects.all()
    }
    # django knows templates folder by default
    return render(request, 'blog/home.html', obj)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # blog/PostViewType.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


def about(request):
    # return HttpResponse("<h1> blog about </h1>")
    return render(request, 'blog/about.html', {'title': "About"})
