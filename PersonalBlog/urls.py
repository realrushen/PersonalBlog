"""PersonalBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog.views import *

urlpatterns = [
    path('', index, name='index'),
    path('posts/create/', PostCreate.as_view(), name='post_create_url'),
    path('posts/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('posts/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('posts/<str:slug>/', PostDetails.as_view(), name='post_details_url'),

    path('tags/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tags/', tags_list, name='tag_list_url'),
    path('tags/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tags/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
    path('tags/<str:slug>/', TagPosts.as_view(), name='tag_posts_page_url'),

    path('admin/', admin.site.urls),
]
