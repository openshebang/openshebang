from django.shortcuts import render

# Dion:

from .models import Notes # This is from the models.py database.

from django.http import Http404 # for the 404

# Create your views here.
def list(request):
    all_notes = Notes.objects.all() # Importa all notes from the database.
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, pk):
    try:
      note = Notes.objects.get(pk=pk) # The `pk` is the primary key for the entry in the database table.
    except Notes.DoesNotExist:
       raise Http404("Note doesn't exist") # The "Note doesn't exist" is not seen.
    return render(request, 'notes/notes_detail.html', {'note': note}) # The second note is the variable created above

