"""Tests of API respi."""
import pytest
import requests


def test_environment(factory_app):
    """Test of the application environment."""
    assert factory_app.environment == 'testing'


# Note: Redis must be started in localhost
# Else it will throw a status code 500
@pytest.mark.parametrize('http_method,http_path', (
    ('GET', '/api/products/'),
))
def test_products(http_method, http_path, flask_app_client):
    """Test of ByeWorld class."""
    response = flask_app_client.open(method=http_method, path=http_path)
    data = requests.get('https://servicespub.prod.api.aws.grupokabum.com.br/descricao/v1/descricao/produto/85197')
    assert response == data.json()
