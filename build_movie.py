from datetime import datetime
import re
from pony.converting import str2datetime
from pony.orm import *
db = Database()

class Movie(db.Entity):
    fname = PrimaryKey(str)
    dt = Optional(str)    # string representation of datetime
    title = Optional(str)
    eventtype = Optional(str)

sql_debug(True)
db.bind(provider='sqlite', filename='rassle/rassle.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


def fname_to_dt(fn):
    regex = 'VID_(\d{8}_\d{6})'
    format_in = '%Y%m%d_%H%M%S'
    format_out = '%Y-%m-%d %H:%M:%S'
    dt = ''
    m = re.match(regex, fn)
    if m:
        match = m.group(1)
        t = datetime.strptime(match,format_in)
        dt = datetime.strftime(t, format_out)
    return dt


@db_session
def populate():
    import boto3
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('wrestling-pics')
    for obj in bucket.objects.all():
        fname = obj.key
        try:
            print("looking for %s" % fname)
            m = Movie[fname]
        except ObjectNotFound:
            dt = fname_to_dt(fname)
            et = 'practice'
            title = fname
            if dt:
                title = dt
            title = et + ' ' + title
            print("inserting %s" % fname)
            m = Movie(fname=fname, dt=dt, title=title, eventtype=et)

populate()    

