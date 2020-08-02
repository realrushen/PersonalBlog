from django.shortcuts import render
from django.views.generic import View

from .models import Post


class MainPage(View):
    pass

def post_details(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_details.html', context={'post': post})


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})
