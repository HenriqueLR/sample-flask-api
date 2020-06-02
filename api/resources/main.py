"""Entrypoint of the main API Resources."""
# Useful to simulate a long action
import requests

from time import sleep

from flask_restplus import Resource, Namespace

from api import factory


api = Namespace(name='', description='Main API namespace.')


celery = factory.celery


@api.route('/products/')
class Products(Resource):
    """Products resource class."""

    def get(self):
        """Get method."""
        # Asynchronous long task that we don't need to know the output
        response = requests.get('https://servicespub.prod.api.aws.grupokabum.com.br/descricao/v1/descricao/produto/85197')
        self.asynchronous.apply_async((response.status_code,))
        return response.json()

    @staticmethod
    @celery.task()
    def asynchronous(status):
        """Async long task method."""
        sleep(5)
        return {'async': status}
