from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-date_posted')[:5]  # Display latest 5 posts
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def blog(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog/blog.html', {'posts': posts})