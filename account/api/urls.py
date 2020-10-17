from django.urls import path
from django import views
from account.api.views import registration_view
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token
#
urlpatterns = [
    path('register',registration_view,name='register-api'),
    path('login',obtain_auth_token,name='login-api'),

 ]