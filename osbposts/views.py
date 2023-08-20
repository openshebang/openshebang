# obsposts\views.py

from django.shortcuts import render # Default

#  DDK
from django.http import HttpResponse

# Create your views here.

def posts_index(request):
    return HttpResponse("Hi from osbposts, the builtin repsonse")

