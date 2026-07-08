from django.shortcuts import get_object_or_404, redirect, render
from .forms import BlogPostForm, CategoryForm
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
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
            
            post=form.save(commit=False) #temporarily saving the form
            post.author=request.user
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