import morepath
from .app import App
from .model import db
from pony.orm import sql_debug


def run():
    sql_debug(True)
    db.bind(provider='sqlite', filename='rassle.sqlite', create_db=True)
    db.generate_mapping(create_tables=True)
    
    morepath.autoscan()
    morepath.run(App())


if __name__ == '__main__':
    run()
