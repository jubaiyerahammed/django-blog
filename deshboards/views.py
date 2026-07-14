from django.shortcuts import get_object_or_404, redirect, render
from .forms import AddUserForm, BlogPostForm, CategoryForm, EditUserForm
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='login')  #এটা Django‑র একটা ডেকোরেটর।
#এটা কোনো ভিউ ফাংশনের উপরে বসালে সেই ভিউ শুধু লগইন করা ইউজারই দেখতে পারবে।
def deshboard(request):
    category_count=Category.objects.all().count()
    blog_count=Blog.objects.all().count()
    context={
        'category_count':category_count,
        'blog_count':blog_count,
    }
    return render (request, 'deshboard/deshboard.html', context)

def categories(request):
    return render (request, 'deshboard/categories.html')

def add_category(request):
    if request.method == 'POST':
        form= CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('categories')

    form= CategoryForm()
    context={
        'form':form
    }
    return render(request, 'deshboard/add_category.html', context)

def edit_category(request,pk):
    category= get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form':form,
        'category':category
    }
    return render (request, 'deshboard/edit_category.html', context)

def delete_category(request, pk):
    category= get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')
 
def posts (request):
    posts=Blog.objects.all()
    context={
        'posts':posts
    }
    return render (request, 'deshboard/posts.html', context)

def add_post(request):
    if request.method=='POST':
        form=BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # temporarily saving the form
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')
        else:
            print('form is invalid')
            print(form.errors)

        
    form= BlogPostForm()
    context={
        'form':form
    }
    return render (request, 'deshboard/add_post.html', context)

def edit_post(request, pk):
    post=get_object_or_404(Blog,pk=pk)
    if request.method=='POST':
        form=BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')  
    form= BlogPostForm(instance=post)
  
    context={
        'form':form,
        'post':post
    }
    return render (request, 'deshboard/edit_post.html', context)


def delete_post(request, pk):
    post= get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')

def users(request):
    users= User.objects.all()
    context={
        'users':users
    }
    return render (request, 'deshboard/users.html', context)

def add_user (request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form=AddUserForm()
    context={
        'form':form,
    }
    return render (request, 'deshboard/add_user.html', context)

def edit_user(request, pk):
    user= get_object_or_404(User, pk=pk)
    if request.method=='POST':
        form=EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form=EditUserForm(instance=user)
    context={
        'form':form,
    }
    return render (request, 'deshboard/edit_user.html', context)