from . import views
from django.conf.urls import url

from movies.views import directors

urlpatterns = [
    url(
        r'^$',
        views.movies,    # Nombre de la funcion dentro del fichero views.py
        name = 'movies'  # 
    ),
    url(
        r'^(?P<movie_id>\d+)/detail/$',
        views.detail,    # Nombre de la funcion dentro del fichero views.py
        name = 'detail'  #
    ),
    url(
        'directors/',
        views.directors,
        name = 'directors'
    )
]