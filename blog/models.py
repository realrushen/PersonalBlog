from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True, blank=False)
    slug = models.SlugField(db_index=True, unique=True)
    preview_text = models.CharField(max_length=200)
    text = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug
