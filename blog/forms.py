from django import forms
from django.core.exceptions import ValidationError

from blog.models import Tag, Post


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug can\'t be \"create\"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Tag with slug "{new_slug}" already exists. Slug must be unique.')
        return new_slug


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'preview_text',
            'text',
            'tags',
            'author',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'preview_text': forms.Textarea(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug can\'t be \"create\"')
        return new_slug
