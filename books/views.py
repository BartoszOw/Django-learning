from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Author, Borrow
from .forms import ReturnBookForm, CommentForm
from django.contrib import messages

# Create your views here.

class BookDetailsView(DetailView):
    model = Book
    template_name = 'book_details.html'
    context_object_name = 'book'

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        if 'comment_form' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.book = book
                comment.save()
                messages.success(request, "Comment Added!")
            else:
                messages.error(request, "Error, no comment added")
        
        elif 'borrow_form' in request.POST:
            borrows = Borrow.objects.filter(book=book, is_returned=False)
            if borrows.exists():
                messages.error(request, f"This book is already borrowed")
            else:
                Borrow.objects.create(book=book, user=request.user)
                messages.success(request, f"You have Successfully borrowed that book")
        return redirect('books:book_details', pk=book.pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        borrows = Borrow.objects.filter(book=book, is_returned=False)
        context['borrow_form'] = ReturnBookForm()
        context['borrows'] = borrows
        context['comment_form'] = CommentForm()
        context['book_already_borrowed'] = borrows.exists()
        return context
    
class AuthorDetailsView(DetailView):
    model = Author
    template_name = 'author_details.html'
    context_object_name = 'author'


class BorrowedListView(LoginRequiredMixin, ListView):
    model = Borrow
    template_name = 'user_borrow_list.html'
    context_object_name = 'borrows'

    def get_queryset(self):
        return Borrow.objects.filter(user=self.request.user, is_returned=False)
    
    def post(self, request):
        borrow_id = request.POST.get('borrow_id')
        if borrow_id:
            borrow = Borrow.objects.get(id=borrow_id)
            borrow.is_returned = True
            borrow.save()
            messages.success(request, 'Book returned!')
        return redirect('books:borrow_list')
            