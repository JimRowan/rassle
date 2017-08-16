import logging
import morepath
import waitress
import yaml
import os
from .app import App
from .model import db
from pony.orm import sql_debug


def setup_db(app):
    sql_debug(app.settings.debugging.sql)
    db_params = app.settings.database.__dict__.copy()
    db.bind(**db_params)
    db.generate_mapping(create_tables=True)


def run():
    directive_logger = logging.getLogger('morepath.directive')
    directive_logger.addHandler(logging.StreamHandler())
    directive_logger.setLevel(logging.DEBUG)
    
    with open('settings.yml') as config:
        settings_dict = yaml.load(config)

    App.init_settings(settings_dict)

    morepath.autoscan()
    morepath.commit(App)
    app = App()

    setup_db(app)

    if os.getenv('RUN_ENV') == 'dev':
        morepath.run(app, host='0.0.0.0', port='80')
    else:
        waitress_logger = logging.getLogger('waitress')
        waitress_logger.setLevel(logging.INFO)
        waitress.serve(app, listen="*:80")


if __name__ == '__main__':
    run()
