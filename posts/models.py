from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True,null=False)
    modified = models.DateTimeField(auto_now=True,null=False)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True, default=None)
    author = models.ForeignKey(
        'posts.author',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    tags = models.ManyToManyField('posts.Tag', related_name='posts')

    def __str__(self):
        return f"id:{self.id}, title:{self.title}, content:{self.content}, author:{self.author.id}"


class Author(models.Model):
    nick = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(null=False, unique=True)
    author_bio = models.TextField(blank=True)


    def __str__(self):
        return f'{self.nick}, {self.email}'
    

class Tag(models.Model):
    word = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.word