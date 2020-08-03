from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .models import Post, Tag


def post_details(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    return render(request, 'blog/post_details.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def tag_posts(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'blog/tag_posts.html', context={'tag': tag})


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})
