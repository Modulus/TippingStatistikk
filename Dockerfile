#
# vUps Dockerfile
#

# Pull base image.
FROM ubuntu:14.04

#Add the vUps code to the /var/www/apps/vUps directoy in the docker image
ADD . /var/www/apps/tipping

#For the uwsgi socket
#VOLUME ["/var/www/apps/tipping/tmp/uwsgi.sock"]

# Install Nginx.
RUN apt-get update && apt-get install -y nginx && echo "\ndaemon off;" >> /etc/nginx/nginx.conf

RUN  apt-get update && apt-get install -y python python-pip python-dev nginx uwsgi uwsgi-plugin-python supervisor

#Install python packages
RUN pip install -r /var/www/apps/tipping/requirements.txt


#start the uwsgi server for the flask app
#WORKDIR /var/www/apps/tipping

#Add the configuration for uwsgi and nginx
ADD ./configs/vups_uwsgi_config.ini /etc/uwsgi/apps-available/vups_config.ini
ADD ./configs/vups_nginx /etc/nginx/sites-available/vups_nginx
ADD ./configs/superv.conf /usr/local/supervisord.conf

#Remove default sites-enabled from nginx with symbolic links
RUN rm /etc/nginx/sites-enabled/default
RUN rm /etc/nginx/sites-available/default

#Add symbolic links
RUN ln -s /etc/nginx/sites-available/vups_nginx /etc/nginx/sites-enabled/vups_nginx
RUN ln -s /etc/uwsgi/apps-available/vups_config.ini /etc/uwsgi/apps-enabled/vups_config.ini



# Define working directory.
WORKDIR /var/www/apps/tipping

CMD ["supervisord", "-n"]
# Expose ports.
EXPOSE 8080
