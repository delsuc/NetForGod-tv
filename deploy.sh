#!/bin/sh

echo "This scripts creates the required directories and copy the file into the live site" 
. configuration.sh

set -v on
# clean left-overs
rm *.pyc

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

# finally, instal crontab - 
crontab -l > previous_crontab
tail -n +2 crontab_eg | crontab -
