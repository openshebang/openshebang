# /osbposts/urls.py 
# DDK: This file is manually created.

from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts_index, name='posts_index'),
]
