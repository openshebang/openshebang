# Dion import:

from django.urls import path

from . import views

urlpatterns = [
  path('home', views.home), # This was originally in the `urls.py` in the project folder.
  path('authorized', views.authorized) # This is for authorization.
]
