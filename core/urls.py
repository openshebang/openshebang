# core\urls.py # DDK
from django.contrib import admin # default 
from django.urls import path # default

# DDK Imported:
from django.views.generic import TemplateView # DDK
from django.urls import include # DDK
from osbposts import views # Deze is nodig om de views.py in te lezen van de 'osbposts'-app.
from osb_cases import views # Deze is nodig om de URLs van een andere app te kunnen aanspreken.

from django.conf import settings
from django.conf.urls.static import static

"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings # Deze 1, is nodig voor 'static' files nodig te maken in osb_cases-app
from django.conf.urls.static import static #  Deze 2, is nodig voor 'static' files bruikbaar te maken in osb_cases-app

urlpatterns = [
    path('admin/', admin.site.urls),
    # DDK
    path('about/', TemplateView.as_view(template_name="about.html")),
    path('index/', TemplateView.as_view(template_name="index.html")),
    # osbposts app
    # path('osbposts/', include('osbposts.urls')), # DDK: Import the url,py file from 'obsposts'.
    # path('osbposts/', views.posts_index),  # De `osbposts/` is de URL, de `views` is de
    path('osbposts/', include('osbposts.urls')), # Dit is nodig om alle URLs die beginnen met 'osbposts' door te sturen naar de osbposts app, en daar alle urlpatterns in de urls.py file in die app...
    path('osb_cases/', include('osb_cases.urls')), # De eerste osb_cases is de URL, de tweede is de folder en de urls is de `urls.py` die in de app zit.
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Deze 3 is nodig voor 'static' files bruikbaar te maken in osb_cases-app.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Deze is nodig voor 'media' files bruikbaar te maken in osb_cases-app.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # werkt deze wel !?
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)