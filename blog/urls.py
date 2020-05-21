"""drdoproject URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_detail/<slug:slug_text>/', views.post_detail, name='post_detail'),
    path('all_articles/', views.allArticles, name='all_articles'),
    path('recruitment_articles/', views.recruitmentArticles, name='recruitment_articles'),
    path('recruitment_post_detail/<slug:slug_text>/', views.recruitment_post_detail, name='recruitment_post_detail'),
    path('editor/', views.editor, name='editor'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_recruitment_post/', views.create_recruitment_post, name='create_recruitment_post')
]
