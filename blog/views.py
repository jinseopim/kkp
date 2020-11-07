from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import HttpResponse


def login_page(request):
    return render(request, "blog/home.html")


def post_list(request):
    print("timezone.now() : ", timezone.now())
    print("Post.objects : ", Post.objects.filter().order_by('published_date'))

    posts = Post.objects.filter().order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})


