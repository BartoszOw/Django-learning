from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def posts_list(request):
    form = PostForm()
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Dodano post')
            return redirect(request.path)
        else:
            messages.error(request,'Cos poszlo nie tak')
    

    
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

@login_required
def posts_editing(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Edytowano post!")
            return redirect('posts:list')
    else:
        form = PostForm(instance=post)        
    return render(request,'post_editing.html', {'post': post, 'form': form})

def author_list(request):
    

    if request.method == 'POST':
        form = AuthorForm(data=request.POST)

        if form.is_valid():
            ex_authors = Author.objects.filter(**form.cleaned_data)
            if ex_authors.exists():
                messages.error(request,'Istnieje juz taki Autor!')
            else:
                form.save()
                messages.success(request,'Dodano autora!')
                return redirect(request.path)
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
