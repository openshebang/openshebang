from django.db import models

# DDK
from django.conf import settings # Deze is nodig om de `settings` te kunnen gebruiker voor de `writer` van een artikel.

# Create your models here.

class post(models.Model):
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Gebruik deze voor de auteur. De naam staat al in de database en als de gebruiker zijn naam verandert, blijft deze ook bestaan.