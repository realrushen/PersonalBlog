from django.shortcuts import render
from django.views.generic import View

from .models import Post, Tag
from .utils import ObjectDetailMixin


class PostDetails(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_details.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagPosts(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_posts.html'


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})
