"""smartnotes URL Configuration

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
from django.contrib import admin
from django.urls import path

# Dion imports:
# from home import views # The first is the project 'app' and the seconds is the 'views.py' file there.

from django.urls import include # The `include` function is used so you don't have to add to the `urlpatterns`-list in this file, but use the `urlpatterns`, from the app, from that specific user created `urls.py`-file.

urlpatterns = [
    path('admin/', admin.site.urls),

    # Dion urlpatters:
    # path('home', views.home) # The first is the URL path and the second is the `home` function in the `views` file, that has been imported above.
    path('', include('home.urls')), # The first `home` is the app, the `urls` is the `urls file`, the `include` has to be improted by Django above.
]
