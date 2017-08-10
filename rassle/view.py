from .app import App
from . import model


@App.html(model=model.Root, template='index.pt')
def view_root(self, request):
    return {
        'movies': self.movies,
        'request': request,
    }


@App.html(model=model.Movie, template='movie.pt')
def view_movie(self, request):
    return {
        'title': self.title,
        'mp4': self.mp4,
    }
