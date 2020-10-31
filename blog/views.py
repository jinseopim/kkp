from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    print("timezone.now() : ", timezone.now())
    print("Post.objects : ", Post.objects.filter().order_by('published_date'))

    posts = Post.objects.filter().order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})


