from django.shortcuts import render

# Dion imports:
from django.http import HttpResponse # Added

from django.contrib.auth.decorators import login_required # This is to assure that users log in.

# Dion additional fun import:
from datetime import datetime

from django.views.generic import TemplateView # For using a Class-view in stead of a Function-view.

from django.contrib.auth.mixins import LoginRequiredMixin # If you want authentication in a Class-view # Mixins-classes are helper classes.
# Create your views here.
def home(request):
  # return HttpResponse('Hello World!')
  return render(request, 'home/welcome.html', {'calculation': 1+1, 'today': datetime.today()}) # The `render` is by default imported, 3 arguments have to be given: 1. The name of the request itself 2. the html template name 3. additionan info

# This decorator is a reserved name, and is imported above
@login_required(login_url='/admin')
def authorized(request):
  return render(request, 'home/authorized.html', {})

class HomeView(TemplateView):
  template_name = 'home/welcome.html' # This is a prefedined method.
  style = 'from a Class, not a Function!' # Dion's variable
  extra_context = {'today': datetime.today(),'view_style': style}

class AuthorizedView(LoginRequiredMixin, TemplateView): # Mixins are helper views. Make sure you start with the LoginRequiredMixin
  template_name = 'home/authorized.html'
  login_url = '/admin' # `login_url` is default term, where the user should go if not logged in.
  style = 'from a Class, not a Function!' # Dion's variable
  extra_context = {'view_style': style}