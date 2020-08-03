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

from blog.views import index, post_details,tag_posts, tags_list

urlpatterns = [
    path('', index, name='index'),
    path('post/<str:slug>/', post_details, name='post_details_url'),
    path('tags/', tags_list, name='tag_list_url'),
    path('tags/<str:slug>/', tag_posts, name='tag_posts_page_url'),
    path('admin/', admin.site.urls),

]
