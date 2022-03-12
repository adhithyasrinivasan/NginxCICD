#Ubuntu base image
FROM ubuntu:18.04

RUN apt-get update && apt-get -y install nginx curl

ADD index.html /usr/share/nginx/html/index.html
ADD server.conf /etc/nginx/conf.d/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]