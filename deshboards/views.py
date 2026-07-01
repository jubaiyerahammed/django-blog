from django.shortcuts import render
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