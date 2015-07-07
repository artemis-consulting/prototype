FROM ubuntu:14.04

# Install dependencies
RUN apt-get update -y
RUN apt-get install -y git curl apache2 build-essential checkinstall python python-setuptools memcached  postgresql postgresql-contrib  python-psycopg2 libpq-dev libapache2-mod-wsgi

# Install pip's dependency: setuptools:
RUN apt-get install -y python python-dev python-distribute python-pip libpq-dev  python-dev

# Install app
RUN rm -rf /apps
RUN mkdir /apps/
RUN mkdir /apps/prototype
ADD code /apps/prototype

#Install PIP dependencies
#RUN pip install -r /var/www/code/requirements.txt


RUN pip install -I Django==1.8.2
RUN pip install -I wsgiref==0.1.2
RUN pip install -I requests==2.7.0

# Used for http server
RUN pip install -I argparse==1.2.1
RUN pip install -I gunicorn==19.3.0

# Used to serve static files
RUN pip install -I whitenoise==2.0

# Used for testing
RUN pip install -I django-nose==1.4
RUN pip install -I mock==1.0.1
RUN pip install -I nose==1.3.7
RUN pip install -I selenium==2.46.0
RUN pip install -I coverage==3.7.1
RUN pip install -I django-coverage==1.2.4

# Used to support memcached
RUN pip install -I python-memcached==1.54

# Used for postgresql
RUN pip install -I psycopg2==2.6.1
RUN pip install -I dj-database-url==0.3.0


# Configure apache
RUN a2enmod rewrite
RUN chown -R www-data:www-data /apps/prototype
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid
EXPOSE 80

RUN rm -rf /etc/apache2/sites-enabled/*
ADD  apache-config.conf /etc/apache2/sites-enabled/000-default.conf


# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/apache2/access.log
RUN ln -sf /dev/stderr /var/log/apache2/error.log





CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]


#CMD /usr/sbin/apache2ctl -D FOREGROUND
#CMD service apache2 start

