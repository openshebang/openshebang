from django.db import models

# Create your models here.

class case(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='user_uploads/') # De `upload_to` is waar het opgeslagen wordt. # Deze `images/` zit direct onder de `Project`-folder (dus niet in de `app`-folder)
    summary = models.CharField(max_length=300)

    def __str__(self): # This 
        return self.summary # The summary is given above! This is thus the alternative, than adding stuf to the admin.py file, to show a text field rather than `Object(x)` in the Object panel.

