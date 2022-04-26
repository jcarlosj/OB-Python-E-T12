from django.db import models
from django.urls import reverse

# Director Model
class Director( models.Model ) :
    first_name = models.CharField( max_length = 100 )
    last_name = models.CharField( max_length = 100 )
    date_of_birth = models.DateField( null = True, blank = True )
    date_of_death = models.DateField( 'Died', null = True, blank = True )

    def get_absolute_url( self ) :
        return reverse( 'director-detail', args=[ str( self.id ) ] )

    def __str__( self ) :
        return f'{ self.first_name } { self.last_name } ({ self.date_of_birth })'

# Movie Model
class Movie( models.Model ) :
    title = models.CharField( max_length = 32 )
    director = models.ForeignKey( 
        Director,                       # Relacion: Con el Modelo Director (Haciendo uso de una llave foranea)
        on_delete = models.SET_NULL,    # Permite eliminar el director del registro
        null = True                     # Permite que este campo sea nulo (Mantiene la integridad relacional)
    )
    synopsis = models.TextField( max_length = 250, help_text = 'Breve sinópsis de la película')
    release_date = models.DateField( null = True, blank = True )

    def get_absolute_url( self ) :
        return reverse( 'movie-detail', args=[ str( self.id ) ] )

    def __str__( self ) :
        return f'{ self.title } ({ self.director })'