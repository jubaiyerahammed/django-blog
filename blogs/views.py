from django.shortcuts import render
from django.http import HttpResponse

from blogs.models import Blog
# Create your views here.

def post_by_category(request, category_id ):

    posts = Blog.objects.filter( status='Published', category=category_id)
    context = {
        'posts':posts,
    }
    return render(request, 'post_by_category.html', context)
