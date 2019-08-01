from django.shortcuts import render
from .models import Post, Category

# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category_name):
    category = Category.objects.get(name=category_name)
    posts = Post.objects.filter(
        categories__name__contains=category_name
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, url):
    post = Post.objects.get(url=url)
    # comments = Comment.objects.filter(post=post)
    context = {
        "post": post
    }
    return render(request, "blog_detail.html", context)