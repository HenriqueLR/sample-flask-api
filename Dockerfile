FROM matthieugouel/python-gunicorn-nginx:latest
MAINTAINER Henrique Luz Rodrigues <henrique.lr89@gmail.com>

# Set the environment package
ENV APP_ENVIRONMENT production

# Copy the package requirements
COPY requirements.txt /tmp/

# Install the package requirements
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

# Copy the application
COPY . /app
