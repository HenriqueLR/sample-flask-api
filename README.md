# Sample flask api asynchronous tasks with celery usage Python3

[![Build Status](https://travis-ci.org/matthieugouel/python-flask-celery-example.svg?branch=master)](https://travis-ci.org/matthieugouel/python-flask-celery-example)
[![Coverage Status](https://img.shields.io/coveralls/github/matthieugouel/python-flask-celery-example.svg)](https://coveralls.io/github/matthieugouel/python-flask-celery-example?branch=master)
[![license](https://img.shields.io/github/license/matthieugouel/python-flask-celery-example.svg)](https://github.com/matthieugouel/python-flask-celery-example/blob/master/LICENSE)

This project is an example of using Flask-restful and celery to perform asynchronous tasks.

## Installation

Note : It's cleaner to use docker-compose to start the whole application (see the section below).

## Dependencies

```
Docker-compose
Docker

if you are using ubuntu run the command 'apt install docker-compose'

for more information see https://phoenixnap.com/kb/install-docker-compose-ubuntu
```

## Usage with Docker Compose

In order to start the whole system easily, we can use docker-compose :

```
docker-compose up -d
```

It will start three docker containers :
- Redis
- Flask API
- Celery Worker

Then, you can access to the API in localhost :

```
curl -X GET -H "Content-Type: application/json" localhost:5000/api/products/
```

## Syntax

You can check the syntax using flake8 (you must have flake8 package installed first) :

```
flake8 api
```

You can also use tox (you must have tox package installed first) :

```
tox -e lint
```

## Test coverage

To execute the test coverage, you must install the package with the dev requirements (see installation section).

You can run the coverage with the following command :

```
entry path api and run command - coverage run --source api -m py.test
```