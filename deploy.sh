#!/bin/sh
echo "This scripts creates the required directories and copy the file into the live site" 
set -v on

. configuration.sh

# clean left-overs
rm *.pyc

# create configuration.php from configuration.sh
python config_mirror.py

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

# create language utilities
pyrhon langues.py
mv langues.js www/js
mv langues.php www/prgm

# finally, instal crontab, but before save previous ones
crontab -l > previous_crontab
tail -n +2 crontab_eg | crontab -
