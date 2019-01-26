
FROM debian:latest


RUN apt-get update && apt-get install -y apache2 \
    libapache2-mod-wsgi \
    build-essential \
    python \
    python-dev\
    python-pip \
    vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*


COPY ./app/requirements.txt /var/www/apache-flask/app/requirements.txt
COPY ./apache-flask.conf /etc/apache2/sites-available/apache-flask.conf
COPY ./apache-flask.wsgi /var/www/apache-flask/apache-flask.wsgi
COPY ./run.py /var/www/apache-flask/run.py
COPY ./app /var/www/apache-flask/app/

RUN pip install -r /var/www/apache-flask/app/requirements.txt
RUN a2ensite apache-flask
RUN a2enmod headers
RUN a2dissite 000-default.conf
RUN a2ensite apache-flask.conf

EXPOSE 80

WORKDIR /var/www/apache-flask

CMD  /usr/sbin/apache2ctl -D FOREGROUND

