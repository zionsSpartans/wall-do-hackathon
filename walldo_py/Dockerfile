FROM python:3.6-alpine

# Install SSH client
RUN apk add openssh-client

# Elasticsearch deps
RUN pip3 install elasticsearch pymongo

# Copy walldo code
COPY ./walldo /walldo

WORKDIR /walldo

# Durante el desarrollo arrancar con:
#   docker run --rm -it -v ${PWD}/walldo:/walldo walldopy /bin/sh

# ENTRYPOINT temporal
ENTRYPOINT ["/bin/sleep","10000000000000000"]
