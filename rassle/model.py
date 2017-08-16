from pony.orm import *
from datetime import datetime

db = Database()


class Login(object):
        pass


class Root(object):
    @property
    @db_session
    def movies(self):
        res = select(m for m in Movie)
        return res


class Movie(db.Entity):
    fname = PrimaryKey(str)
    dt = Optional(str)    # string representation of datetime
    title = Optional(str)
    eventtype = Optional(str)
