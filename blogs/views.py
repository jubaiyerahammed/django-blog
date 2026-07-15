from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from blogs.models import Blog, Category, Comment
from django.db.models import Q
# Create your views here.

def post_by_category(request, category_id ):

    posts = Blog.objects.filter( status='Published', category=category_id, author=request.user)
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect the user to homepage
    #     return redirect('home')
    category=get_object_or_404(Category,pk=category_id)
    context = {
        'posts':posts,
        'category':category,
    }
    return render(request, 'post_by_category.html', context)

def blogs(request, slug):
    single_blog=get_object_or_404(Blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    #Comments
    comments= Comment.objects.filter(blog=single_blog)
    comment_count=comments.count()
    context={
        'single_blog':single_blog,
        'comments':comments,
        'comment_count':comment_count,
    }
    return render(request, 'blogs.html', context)

def search(request):
    query = request.GET.get('query')
    
    blogs = Blog.objects.filter(Q(title__icontains=query) | Q(short_description__icontains=query) | Q(blog_body__icontains=query), status='Published')

    context = {
        'query': query,
        'blogs': blogs
    }
    return render(request, 'search.html', context)
