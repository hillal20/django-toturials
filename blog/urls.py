from django.urls import path
from . import views
from .views import PostListView
urlpatterns = [

    # path('', views.home, name='blog-home'), # original version before we use PostListView-built-in way
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
]

# important
# <app>/<model>_<viewType>.html === blog/PostViewType.html
