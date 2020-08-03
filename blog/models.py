from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_posts_page_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(db_index=True, unique=True)
    preview_text = models.CharField(max_length=200)
    text = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def get_absolute_url(self):
        return reverse('post_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.slug
