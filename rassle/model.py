from pony.orm import *
from datetime import datetime

db = Database()


class Root(object):
    @property
    @db_session
    def movies(self):
        res = select(m for m in Movie)
        return res


class Movie(db.Entity):
    fname = PrimaryKey(str)
    dt = Optional(datetime)
    title = Optional(str)
