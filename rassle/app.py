from more.chameleon import ChameleonApp
from more.pony import PonyApp

class App(ChameleonApp, PonyApp):
    pass


@App.template_directory()
def get_template_directory():
    return 'templates'


@App.setting_section(section='chameleon')
def get_chameleon_settings():
    return {'debug': True}
