# obsposts\views.py

from django.shortcuts import render # Default

#  DDK
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required # Deze is nodig om de @ voor de login required te crearen.
from .models import post # DDK
from django.http import Http404

# Create your views here.

def posts_index(request):
    return render(request, 'osbposts/posts.html', {'calculatie': 1+1}) # In de eerste 'calculatie' geven we de variabele mee die wel aan de DTL meegegeven, de tweede is de waarde van die variabele (die kan ook hierboven gefinieerd worden).
    #return HttpResponse("Hi from osbposts, the builtin repsonse")

@login_required
def authorized(request):
    return render(request, 'osbposts/authorized.html', {})

def posts_all(request):
    allposts = post.objects.all() # Imports all posts from the database.
    return render(request, 'osbposts/posts_all.html', {'posts': allposts})

def posts_single(request, post_id):
  try: # try and execpt, zodat een nette 404 error wordt gegereneerd.
    singlepost = post.objects.get(id=post_id) # De eerste `id` zit gewoon in de database, in Djano is het kennelijk beter om `pk` voor primary key te gebruiken, echter zit deze NIET in de database.
    creatie_datum = str(singlepost.created_at)
    update_datum = str(singlepost.updated_at)
    if creatie_datum[0:16] == update_datum[0:16]: 
      post_updated = ''
    else:
      post_updated = 'Updated: ' + update_datum[0:16]
  except:
    raise Http404("Post does not exist")      
  return render(request, 'osbposts/posts_single.html', {'post' : singlepost, 'updated_time' : post_updated })
