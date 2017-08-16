import morepath
from .app import App
from . import model
from webob.exc import HTTPForbidden


class ViewPermission(object):
    pass


@App.permission_rule(model=model.Movie, permission=ViewPermission)
def document_view_permission(identity, model, permission):
    return identity in ['jmr']


@App.view(model=HTTPForbidden)
def make_unauthorized(self, request):
    @request.after
    def set_status_code(response):
        response.status_code = 401
        response.www_authenticate = "Bearer"

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


@App.html(model=model.Movie, template='movie.pt', permission=ViewPermission)
def view_movie(self, request):
    return {
        'title': self.title,
        'fname': self.fname,
    }


@App.html(model=model.Login, template='login.pt')
def view_login(self,request):
    return {}


from webob.exc import HTTPProxyAuthenticationRequired
@App.view(model=model.Login, request_method='POST')
def login(self, request):
    username = request.POST['username']
    #password = request.POST['password']

    # Do the password validation.
    #if not user_has_password(username, password):
    if not username == 'jmr':
        raise HTTPProxyAuthenticationRequired('Invalid username/password')

    @request.after
    def remember(response):
        # We pass the extra info to the identity object.
        #identity = morepath.Identity(username, email=email, role=role)
        identity = morepath.Identity(username)
        request.app.remember_identity(response, request, identity)

    return "You're logged in."  # or something more fancy
