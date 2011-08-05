#!/bin/sh

# This scripts creates the required directories and copy the file into the live site 
. configuration.sh


# create directories
# first local for logs
mkdir -p logs

# first WEBROOT
mkdir -p $WEBROOT

# then subfolders
mkdir -p $VIDEOdir
mkdir -p $VODdir

# then utilities
for i in css js prgm s; do
    mkdir -p $WEBROOT/$i
    cp www/$i/* $WEBROOT/$i
done

