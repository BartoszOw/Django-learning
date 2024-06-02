from django.contrib import admin
from books.models import Tag, Author, Book

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'author_id']
    list_filter = ['title', 'tags', 'author_id']
    search_fields = ['title', 'tags', 'author_id']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','name','surname','author_bio']
    search_fields = ['name', 'surname']
    list_filter = ['name', 'surname']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'word', 'created']
    search_fields = ['word']
    list_filter = ['word']