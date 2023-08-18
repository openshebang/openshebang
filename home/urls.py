# Dion import:

from django.urls import path

from . import views

urlpatterns = [
  path('home', views.home), # This was originally in the `urls.py` in the project folder.
  path('authorized', views.authorized), # This is for authorization.
  path('home_class', views.HomeView.as_view()), # This is if a Class-view has been used in stead of a Function-view.
  path('authorized_class', views.AuthorizedView.as_view()) 
]
