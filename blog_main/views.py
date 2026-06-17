from django.shortcuts import render

from about.models import About
from blogs.models import Category, Blog 

def home (request):
    #categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')[:3]
    posts= Blog.objects.filter(is_featured=False, status='Published')

    try:
        about=About.objects.get()
    except:
        about=None    
    context ={
        #'categories':categories,
        'featured_posts':featured_posts,
        'posts': posts,
        'about':about
    }
    return render( request, 'home.html', context )

def search(request):
    query = request.GET.get('q', '')
    results = Blog.objects.filter(title__icontains=query)

    context = {
        'query': query,
        'results': results
    }
    return render(request, 'search.html', context)