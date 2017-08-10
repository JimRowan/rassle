class Root(object):
    @property
    def movies(self):
        import boto3
        movies = []
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('wrestling-pics')
        for obj in bucket.objects.all():
            movies.append(Movie(obj.key))
        return movies

class Movie(object):
    def __init__(self, mp4):
        self.mp4 = mp4
        self.title = mp4


