from django.urls import path
from django import views
from . import views
from django.contrib.auth import views as auth_views
#
urlpatterns = [
    path('',views.blog_index,name='blog_index'),
    path('create/',views.create_blog,name='blog_create'),
    path('blog/<slug>',views.detail_blog_view,name='blog_detail'),
    path('edit/<slug>',views.update_blog_post,name='blog_edit'),

 ]