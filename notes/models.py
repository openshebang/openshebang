from django.db import models

# Create your models here. # As a class. # After the creation of the model class, you run `python3 manage.py makemigrations`
class Notes(models.Model): # The `model` is imported above, and the Model can be choosen.
  title = models.CharField(max_length=200)
  text = models.TextField()
  created = models.DateTimeField(auto_now_add=True)

