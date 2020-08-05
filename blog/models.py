from time import time

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def generate_unique_slug(string):
    slug = slugify(string)
    return f'{slug}-{str(int(time()))}'


class Tag(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_posts_page_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(db_index=True, unique=True, blank=True)
    preview_text = models.CharField(max_length=200)
    text = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('post_details_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_unique_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def __repr__(self):
        return f'Post({self.id}, {self.title}, {self.slug}, {self.preview_text}, ' \
               f'{self.created}, {self.updated},' \
               f' {self.tags}'
