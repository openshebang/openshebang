from django.contrib import admin # Default

from .models import case # needed to import the model (for the db)


# This is for the admin, maar let op dat je deze eerste moet doen. en dat deze boven de `Register your models here.` moet komen. Let ook op dat de `caseAdmin` Model alleen in deze pagina voorkomt. Je kan deze dus zelf aanpassen.
class caseAdmin(admin.ModelAdmin): # Deze is nodig, anders wordt alleen het nummer/ID van elke post weergegeven, nu kan je gewoon de 'summary' van de post weergeven.
    list_display = ('summary', )

# Register your models here.
admin.site.register(case, caseAdmin) # Dit voegt de 'case' het toe aan de admin site.
