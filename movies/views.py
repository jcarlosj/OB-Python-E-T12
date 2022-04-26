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
def detail( request, movie_id ) :
    movie = Movie.objects.get( id = movie_id )      # Tambien funciona -> movie = Movie.objects.get( pk = movie_id )

    # print( 'movie_id', movie_id )
    # print( type( movie ) )
    # print( 'movie', movie.title, movie.synopsis )

    return render(
        request,
        'detail.html',
        context = {
            'movie': movie
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