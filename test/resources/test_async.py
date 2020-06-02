"""Tests of asynchronous tasks."""
import requests


def test_products_async(byeworld):
    """Test of ByWorld asynchronous task method."""
    data = requests.get('https://servicespub.prod.api.aws.grupokabum.com.br/descricao/v1/descricao/produto/85197')
    task = products.asynchronous.delay(data.status_code)
    assert task.get(timeout=10) == {'async': 200}
