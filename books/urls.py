from django.urls import path
from django.views.generic import ListView
from .views import BookDetailsView, AuthorDetailsView, BorrowedListView
from .models import Book,Author,Tag

app_name = 'books'
urlpatterns = [
    path('all-books', ListView.as_view(model=Book, template_name='books_list.html', paginate_by=5), name='books_list'),
    path('all-authors', ListView.as_view(model=Author, template_name='authors_list.html', paginate_by=5), name='authors_list'),
    path('all-books/<int:pk>/', BookDetailsView.as_view(), name='book_details'),
    path('all-authors/<int:pk>/', AuthorDetailsView.as_view(), name='author_details'),
    path('borrowed-list/', BorrowedListView.as_view(), name='borrow_list')
]