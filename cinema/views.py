from django.shortcuts import render

# Index View: Home Project
def index( request ) :

    return render(
        request,
        'index.html',
        context = {}
    )