"""Setup module of the package."""
import uuid

__author__ = 'Henrique Luz Rodrigues <henrique.lr89@gmail.com>'
from setuptools import setup, find_packages
from pip.req import parse_requirements


INSTALL_REQS = parse_requirements('requirements.txt', session=uuid.uuid1())
REQS = [str(ir.req) for ir in INSTALL_REQS]

setup(
    name="api",
    version="0.1.0",
    packages=find_packages(),
    author="Henrique Luz Rodrigues",
    author_email="henrique.lr89@gmail.com",
    description="api for Python3 projects",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="",
    include_package_data=True,
    install_requires=REQS
)
