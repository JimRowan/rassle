import morepath
import rassle

from webtest import TestApp as Client


def test_root():
    morepath.scan(rassle)
    morepath.commit(rassle.App)

    client = Client(rassle.App())
    root = client.get('/')

    assert root.status_code == 200
    assert '/greeting/world' in root
    assert '/greeting/mundo' in root
