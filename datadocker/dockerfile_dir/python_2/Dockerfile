#!/usr/bin/env bash

# base image
# https://hub.docker.com/r/phusion/baseimage/
FROM phusion/baseimage

# Export env settings
ENV LANG=en_US.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Update the list of packages, upgrade the current packages and install build-essential
ADD /packages/image-packages.txt /tmp/image-packages.txt
RUN apt-get update \
    && apt-get -y build-dep libcurl4-gnutls-dev \
    && xargs -a /tmp/image-packages.txt apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Clean apt-get
RUN apt-get clean \
    && apt-get autoremove

# Install python packages
ADD /packages/requirements/ /tmp/requirements
RUN pip --no-cache-dir install -r /tmp/requirements/requirements.txt

# Create new folders and set a workdir
RUN mkdir /home/datadocker
VOLUME /home/datadocker
WORKDIR /home/datadocker

# Add the running script
ADD /command/run.sh /root/run.sh
RUN chmod +x /root/run.sh

# Export port 8888
EXPOSE 8888

# Run jupyter
CMD ["/root/run.sh"]
