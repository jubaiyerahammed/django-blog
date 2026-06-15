from django.shortcuts import redirect, render
from django.http import HttpResponse

from blogs.models import Blog, Category
# Create your views here.

def post_by_category(request, category_id ):

    posts = Blog.objects.filter( status='Published', category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        # redirect the user to homepage
        return redirect('home')
    
    context = {
        'posts':posts,
        'category':category,
    }
    return render(request, 'post_by_category.html', context)
