from more.chameleon import ChameleonApp
from more.pony import PonyApp

class App(ChameleonApp, PonyApp):
    pass


@App.template_directory()
def get_template_directory():
    return 'templates'
