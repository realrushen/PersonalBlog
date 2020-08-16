from django.db.models import F, Prefetch
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from blog.models import Tag, Post


class ObjectDetailMixin:
    model = None
    template = None
    count_views = False

    def get(self, request, slug):
        if self.count_views:
            self.model.objects.filter(slug__iexact=slug).update(views=F('views') + 1)
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj,
                                                       'admin_panel_object': obj,
                                                       'detail_view': True})


class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, template_name=self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, template_name=self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, template_name=self.template,
                      context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)
        if bound_form.is_valid():
            updated_obj = bound_form.save()
            return redirect(updated_obj)
        return render(request, template_name=self.template,
                      context={'form': bound_form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
