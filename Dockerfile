FROM ubuntu:14.04

RUN echo 'building simple_io container...'

LABEL "Author"="Arfath Pasha"
LABEL "Email"="arfathpasha@gmail.com"
LABEL "Description"="Simple I/O via shared volume"

RUN apt-get update

RUN sudo apt-get -y install python

# add code
RUN mkdir /sample_io

ADD src /sample_io


CMD [ "python", "./python/simple_io.py" ]

