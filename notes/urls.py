# notes/urls.py

# Dion import:
from django.urls import path

from . import views

urlpatterns = [
  path('notes', views.list), # The `views.lists` is the function `lists` created in `urls.py`.
  path('notes/<int:pk>', views.detail), # The `/<int:pk>` will show that an interger with the name `pk` will be used.
]


