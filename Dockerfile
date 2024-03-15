FROM ubuntu
RUN apt-get update -y
RUN apt install apache2 -y
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
 
COPY ./build/ /var/www/html/
 
EXPOSE 80
