from django.shortcuts import render
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm
from django.contrib import messages

# Create your views here.


def posts_list(request):

    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            messages.success(request,'Dodano post')
        else:
            messages.error(request,'Cos poszlo nie tak')
    else:
        messages.error(request, 'Nie udalo sie dodac!')
        
    form = PostForm()
    posts = Post.objects.all()
    return render(
        request=request,
        template_name='post_list.html',
        context={'posts': posts, 'form': form}
    )

def posts_details(request, id):
    post = Post.objects.get(id=id)
    return render(
        request=request,
        template_name='post_details.html',
        context={'post': post}
    )

def author_list(request):
    

    if request.method == 'POST':
        form = AuthorForm(data=request.POST)

        if form.is_valid():
            ex_authors = Author.objects.filter(**form.cleaned_data)
            if ex_authors.exists():
                messages.error(request,'Istnieje juz taki Autor!')
            else:
                Author.objects.create(**form.cleaned_data)
                messages.success(request,'Dodano autora!')
        else:
            messages.error(request,'Nie udalo sie dodac autora')

    form = AuthorForm()
    authors = Author.objects.all()
    return render(
        request=request,
        template_name='author_list.html',
        context={
            'authors': authors,
            'form' : form
            }
    )

def author_details(request, id):
    author = Author.objects.get(id=id)
    return render(
        request=request,
        template_name='author_details.html',
        context={'author': author}
    )
