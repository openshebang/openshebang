from django.contrib import admin

# Dion:
from . import models

# Register your models here.
class NotesAdmin(admin.ModelAdmin): # This is to prepare so you can see the NotesAdmin in the Admin view.
    list_display = ('title', ) # Instead of `Notes object (1)` it will just display the `title` in Django Admin.
    # pass # This will note show a name in the Django Admin, but just `Notes object(1)`.

# Dion: Also needed
admin.site.register(models.Notes, NotesAdmin) # Show the Notes in the Admin, you might need to restart the user.





