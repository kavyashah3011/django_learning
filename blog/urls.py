from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('posts/', views.blogpost),
    path('posts/<slug:blog>/', views.blog_post, name='blog_post')
]
