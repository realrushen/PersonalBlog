from django.contrib import admin

from blog.models import Post, Tag, PostComment

# Register your models here.

admin.site.register(Post)

admin.site.register(Tag)

admin.site.register(PostComment)
