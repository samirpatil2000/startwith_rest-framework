from django.urls import path
from django import views
from . import views
from django.contrib.auth import views as auth_views
#
urlpatterns = [
    path('',views.index,name='home'),
    path('register/',views.registration_view,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('login/',views.login_view,name='login'),
    path('account_view/',views.account_view,name='account_view'),



    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'),
         name='password_change'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html'), name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),

 ]