from more.chameleon import ChameleonApp
from more.pony import PonyApp
from more.jwtauth import JWTIdentityPolicy


class App(ChameleonApp, PonyApp):
    pass


@App.template_directory()
def get_template_directory():
    return 'templates'


@App.setting_section(section="jwtauth")
def get_jwtauth_settings():
    return {
        # Set a key or key file.
        'master_secret': 'secret',
        # Adjust the settings which you need.
        'leeway': 10
}


@App.identity_policy()
def get_identity_policy(settings):
    # Get the jwtauth settings as a dictionary.
    jwtauth_settings = settings.jwtauth.__dict__.copy()

    # Pass the settings dictionary to the identity policy.
    return JWTIdentityPolicy(**jwtauth_settings)


@App.verify_identity()
def verify_identity(identity):
    # As we use a token based authentication
    # we can trust the claimed identity.
    return True
