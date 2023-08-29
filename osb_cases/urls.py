# Dit is een nieuwe file

from django.urls import path # voor de path functie beneden

from . import views # importeer de views.py file

from django.conf import settings # Deze 1, is nodig voor 'static' files nodig te maken in osb_cases-app
from django.conf.urls.static import static #  Deze 2, is nodig voor 'static' files bruikbaar te maken in osb_cases-app

urlpatterns = [
    path('', views.cases_home, name='cases_home'),
    path('<int:case_id>', views.osb_single, name='osb_single'), # You don't have to incluse the 'osb_cases' in front fro the app, as this is already determined in the url.py of the app...
] 

