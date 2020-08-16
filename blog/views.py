from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .forms import TagForm, PostForm
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin


class PostDetails(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_details.html'
    count_views = True


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create.html'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'index'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'


class TagPosts(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_posts.html'

    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        tag_posts = Post.objects.filter(tags__slug__iexact=slug).prefetch_related('tags').select_related('author')
        return render(request, template_name=self.template, context={'tag': tag, 'tag_posts': tag_posts})



class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tag_list_url'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def index(request):
    posts = Post.objects.all().prefetch_related('tags').select_related('author')
    return render(request, 'blog/index.html', context={'posts': posts})
