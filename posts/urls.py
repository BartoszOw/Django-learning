from django.urls import path
from .views import posts_list, posts_details, author_list, author_details

app_name = 'posts'
urlpatterns = [
    path('list/', posts_list, name='list'),
    path('list/<int:id>', posts_details, name='details'),
    path('authors/', author_list, name='a_list'),
    path('authors/<int:id>', author_details, name='a_details'),
]