FROM php:8.4-rc-fpm-alpine

WORKDIR /var/www/html

RUN docker-php-ext-install pdo pdo_mysql