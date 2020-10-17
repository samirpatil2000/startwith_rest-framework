from django.urls import path
from django import views
from account.api.views import registration_view
from django.contrib.auth import views as auth_views
#
urlpatterns = [
    path('register',registration_view,name='register-api'),

 ]