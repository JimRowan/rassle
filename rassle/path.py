from .app import App
from . import model

@App.path(model=model.Root, path='/')
def get_root():
    return model.Root()


@App.path(model=model.Movie, path='/movie/{fname}')
def get_movie(fname):
    return model.Movie.get(fname=fname)
        
