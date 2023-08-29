from django.shortcuts import render
from django.shortcuts import get_object_or_404 # This is needed fro getting the object for the db, or return a 404 if that specific id does not exist.

from .models import case; # Hiermee kunnen we informatie uit de db trekken.

# Create your views here.

def cases_home(request):
    cases = case.objects
    return render(request, 'osb_cases/cases_home.html', {'cases': cases}) # De `osb_cases` is all in de `osb_cases/templates` folder. # De linker 'cases' wordt gebruikt in DTL, de rechter is de variabele (dus de database) die hierboven aangeroepen wordt.

def osb_single(request, case_id): # De tweede is precies de benaming die staat in de URL van de urls.py in the app.
    cases_detail = get_object_or_404(case, pk=case_id) # the`case` is the name of the Model. `pk`, is an internal name we have not created this. I also have not seen this in the database itself. pk= Primary Key
    return render(request, 'osb_cases/cases_single.html', {'case':cases_detail})
