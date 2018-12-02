from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(requests):
    blogs = Blog.objects
    return render(requests, 'blog/allblogs.html', {'blogs': blogs})


def detail(requests, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(requests, 'blog/detail.html', {'blog': detailblog})
