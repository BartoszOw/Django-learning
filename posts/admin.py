from django.contrib import admin
from posts.models import Post, Author, Tag

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','nick','email','author_bio']
    search_fields = ['nick']
    list_filter = ['nick']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','created','modified','author_id']
    search_fields = ['title']
    list_filter = ['title']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'word', 'created']
    search_fields = ['word']
    list_filter = ['word']