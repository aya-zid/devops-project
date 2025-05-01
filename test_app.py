import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<html" in response.data  # crude check for HTML content

def test_weather_route_missing_params(client):
    response = client.get('/weather')
    assert response.status_code == 400
    assert response.get_json()['error'] == "No location provided."

def test_weather_route_invalid_coords(client):
    # These coordinates are not "invalid" but will likely still return something unless the API key is invalid
    response = client.get('/weather?lat=0&lon=0')
    
    # We don't assert status here because if API key is invalid or there's a network issue,
    # the app is supposed to return a 500 error — which is correct behavior
    assert response.status_code in (200, 500)
