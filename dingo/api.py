from rest_framework import routers
from posts import api_views as posts_views
from books import api_views as books_views

router = routers.DefaultRouter()
router.register('posts', posts_views.PostViewSet)
router.register('posts-author', posts_views.AuthorViewSet)
router.register('books', books_views.BookViewSet, basename='books')
router.register('books-creator', books_views.CreatorViewSet, basename='creator')