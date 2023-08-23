# /osbposts/urls.py 
# DDK: This file is manually created.

from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts_index, name='posts_index'), # '' is de URL, 'views' is the views.py-file, post_index is de posts_index view-functie, de laste kan gebruikt worden voor dynamische url (relateerbaar aan Flasks 'url_for').
    path('authorized', views.authorized, name='posts_authorized'), # 
    path('posts_all', views.posts_all, name="posts_all"),
    path('posts_single/<int:post_id>/', views.posts_single, name='posts_single'),
]
