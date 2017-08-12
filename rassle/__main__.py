import morepath
import waitress
import os
from .app import App
from .model import db
from pony.orm import sql_debug


def run():
    sql_debug(True)
    db.bind(provider='sqlite', filename='rassle.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)
    
    morepath.autoscan()
    if os.getenv('RUN_ENV') == 'dev':
        morepath.run(App(), host='0.0.0.0', port='80')
    else:
        waitress.serve(App(), listen="*:80")


if __name__ == '__main__':
    run()
