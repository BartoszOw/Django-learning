from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True,null=False)
    modified = models.DateTimeField(auto_now=True,null=False)
    author = models.ForeignKey(
        'posts.author',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )


class Author(models.Model):
    nick = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(null=False, unique=True)
    author_bio = models.TextField(blank=True)


    def __str__(self):
        return self.nick