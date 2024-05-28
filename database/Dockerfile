FROM mysql:latest

ENV MYSQL_DATABASE=crud_db
ENV MYSQL_ROOT_PASSWORD=1234

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306


