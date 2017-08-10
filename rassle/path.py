from .app import App
from . import model


@App.path(model=model.Root, path='/')
def get_root():
    return model.Root()


@App.path(model=model.Movie, path='/movie/{mp4}')
def get_movie(mp4):
    return model.Movie(mp4)
