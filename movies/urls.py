from . import views
from django.conf.urls import url

from movies.views import directors

urlpatterns = [
    url(
        r'^$',          # /
        views.movies,    # Nombre de la funcion dentro del fichero views.py
        name = 'movies'  # 
    ),
    url(
        'directors/',
        views.directors,
        name = 'directors'
    )
]