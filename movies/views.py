from django.shortcuts import render

from.models import Director, Movie

# Movies View: List Movies
def movies( request ) :

    movies = Movie.objects
    print( movies ) 

    return render(
        request,
        'movies.html',
        context = {
            'movies': movies
        }
    )

# Directors View: List Directors
def directors( request ) :

    directors = Director.objects
    print( directors ) 

    return render(
        request,
        'directors.html',
        context = {
            'directors': directors
        }
    )