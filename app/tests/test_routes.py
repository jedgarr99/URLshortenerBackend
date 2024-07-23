import pytest
from app import create_app, db
from app.models import URL

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_shorten_url(client):
    response = client.post('/shorten', json={'url': 'http://example.com/vsgvcsldvilasvhjvkxvksflvlxhjvcsdljvcxvjlsdvjk/fhvxchjvjxkvjvjkdvx'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'short_url' in data

def test_redirect_url(client):
    with client.application.app_context():
        url = URL(original_url='http://example2.com', short_url='abcd2234')
        db.session.add(url)
        db.session.commit()

    response = client.get('/abcd1234')
    assert response.status_code == 302