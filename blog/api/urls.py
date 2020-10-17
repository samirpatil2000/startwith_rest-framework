from django.urls import path
from django import views
from blog.api.views import api_view,blog_api_detail,blog_api_create,blog_api_delete,blog_api_update
from django.contrib.auth import views as auth_views
#
urlpatterns = [
    path('<slug>/',blog_api_detail,name='blog_api_detail'),
    path('create',blog_api_create,name='blog_api_create'),
    path('<slug>/delete',blog_api_delete,name='blog_api_delete'),
    path('<slug>/update',blog_api_update,name='blog_api_update'),


 ]