from django.urls import path,include
from . import views
from django.contrib import admin

app_name='blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),

] 