from django.urls import path
from .views import posts_list, posts_details, author_list, author_details, posts_editing
from django.views.generic import ListView
from posts.models import Post

app_name = 'posts'
urlpatterns = [
    path('list/', posts_list, name='list'),
    path('list/<int:id>', posts_details, name='details'),
    path('list/edit/<int:id>', posts_editing, name='editing'),
    path('authors/', author_list, name='a_list'),
    path('authors/<int:id>', author_details, name='a_details'),
    path('all-posts/', ListView.as_view(model=Post, template_name='post_list.html'), name='posts_list'),
]