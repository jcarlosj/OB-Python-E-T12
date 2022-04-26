from django.shortcuts import render
from imdb import available_access_systems

# Movies View: List Movies
def movies( request ) :

    return render(
        request,
        'movies.html',
        context = {}
    )

# Directors View: List Directors
def directors( request ) :

    return render(
        request,
        'directors.html',
        context = {}
    )