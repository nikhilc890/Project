FROM php:8.0-apache
COPY . /var/www/html
RUN apt-get update -y && apt-get install -y libmariadb-dev 
RUN docker-php-ext-install mysqli

