from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf
from django.views.generic import View

from .forms import TagForm, PostForm, PostCommentForm
from .models import Post, Tag, PostComment
from .utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin


class PostDetails(View):
    model = Post
    template = 'blog/post_details.html'
    count_views = True
    comment_form = PostCommentForm

    def get(self, request, slug):
        context = {}
        context.update(csrf(request))
        if self.count_views:
            self.model.objects.filter(slug__iexact=slug).update(views=F('views') + 1)
        obj = self.model.objects.get(slug__iexact=slug)
        user = auth.get_user(request)
        context[self.model.__name__.lower()] = obj
        context['admin_panel_object'] = obj
        context['detail_view'] = True
        context['comments'] = PostComment.objects.select_related('author_id',
                                                                 'parent_id',
                                                                 'parent_id__author_id',).filter(
                                                                                           post_slug__slug__iexact=slug)

        if user.is_authenticated:
            context['form'] = self.comment_form
        return render(request, template_name=self.template, context=context)


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create.html'


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'index'


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'


class TagPosts(View):
    model = Tag
    template = 'blog/tag_posts.html'

    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        tag_posts = Post.objects.filter(tags__slug__iexact=slug).prefetch_related('tags').select_related('author')
        return render(request, template_name=self.template, context={'tag': tag,
                                                                     'tag_posts': tag_posts,
                                                                     'admin_panel_object': tag,
                                                                     'detail_view': True})


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tag_list_url'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def index(request):
    post_list = Post.objects.filter(status='published').prefetch_related('tags').select_related('author')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    is_paginated = paginator.num_pages > 1
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page has no objects to show deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', context={'page': page, 'posts': posts, 'is_paginated': is_paginated, })


class PostAddComment(LoginRequiredMixin, View):

    def post(self, request, slug):
        form = PostCommentForm(request.POST)
        post = get_object_or_404(Post, slug=slug)

        if form.is_valid():
            comment = PostComment()
            comment.post_slug = post
            comment.author_id = auth.get_user(request)
            comment.text = form.cleaned_data['comment_area']
            comment.save()
            if form.cleaned_data['parent_comment'] is not None:
                comment.parent_id = PostComment(pk=form.cleaned_data['parent_comment'])
                comment.save()

        return redirect(post.get_absolute_url())
