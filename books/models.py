from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150, null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='books/photos/%Y/%m/%d', null=True, blank=True, default=None)
    author = models.ForeignKey(
        'books.author',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    tags = models.ManyToManyField('books.Tag', related_name='books')


    def __str__(self) -> str:
        return f'{self.title}'

class Author(models.Model):
    name = models.CharField(max_length=150, null=False)
    surname = models.CharField(max_length=150, null=False)
    author_bio = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'
    
class Tag(models.Model):
    word = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.word
    
class Borrow(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(default=timezone.now)
    is_returned = models.BooleanField(default=False)
    return_date = models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.user.username} borrowed {self.book.title}'
    

class Comment(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.author} - {self.book.title}'
