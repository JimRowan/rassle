import morepath
from .app import App, FullPermission
from . import model
from webob.exc import HTTPForbidden


class ViewPermission(object):
    pass


@App.view(model=HTTPForbidden)
def make_unauthorized(self, request):
    @request.after
    def set_status_code(response):
        response.status_code = 401
        response.www_authenticate = 'Basic'
    return "Unauthorized"


@App.html(model=model.Root, template='index.pt')
def view_root(self, request):
    return {
        'movies': self.movies,
        'request': request,
    }


@App.view(model=model.Root, name='robots.txt')
def get_robots(self, request):
    return """User-agent: *
Disallow: /"""


@App.html(model=model.Movie, template='movie.pt', permission=FullPermission)
def view_movie(self, request):
    return {
        'title': self.title,
        'fname': self.fname,
    }
