from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.shortcuts import render


urlpatterns = [
    path("admin/", admin.site.urls),
    path("news/", include('polls.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('accounts/profile/', user_views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
]
