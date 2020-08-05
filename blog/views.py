from django.shortcuts import render
from django.views.generic import View

from .forms import TagForm, PostForm
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin


class PostDetails(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_details.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'


class TagPosts(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_posts.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'

    # def get(self, request, slug):
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     bound_form = TagForm(request.POST, instance=tag)
    #
    #     if bound_form.is_valid():
    #         updated_tag = bound_form.save()
    #         return redirect(updated_tag)
    #     return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})
