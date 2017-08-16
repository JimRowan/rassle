from more.chameleon import ChameleonApp
from more.pony import PonyApp
from more.basicauth import BasicAuthIdentityPolicy
from webob.exc import HTTPForbidden
from .model import Movie


class App(ChameleonApp, PonyApp):
    pass


@App.template_directory()
def get_template_directory():
    return 'templates'


class FullPermission(object):
    pass


@App.permission_rule(model=Movie, permission=FullPermission)
def document_view_permission(identity, model, permission):
    return identity.userid in ['visitor']


@App.identity_policy()
def get_identity_policy():
    return BasicAuthIdentityPolicy()


@App.verify_identity()
def verify_identity(identity):
    # Do the password validation.
    return user_has_password(identity.userid, identity.password)

def user_has_password(userid, password):
    return userid == 'visitor' and password == '6minutes'
