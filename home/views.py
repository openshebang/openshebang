from django.shortcuts import render

# Dion imports:
from django.http import HttpResponse # Added

from django.contrib.auth.decorators import login_required # This is to assure that users log in.

# Dion additional fun import:
from datetime import datetime

# Create your views here.
def home(request):
  # return HttpResponse('Hello World!')
  return render(request, 'home/welcome.html', {'calculation': 1+1, 'today': datetime.today()}) # The `render` is by default imported, 3 arguments have to be given: 1. The name of the request itself 2. the html template name 3. additionan info

# This decorator is a reserved name, and is imported above
@login_required(login_url='/admin')
def authorized(request):
  return render(request, 'home/authorized.html', {})
