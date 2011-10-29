<?php
# This file was automaticaly created from configuration.sh using config_mirror.py - do not edit
# This file contains all the configuration parameters for the FOI project
# Any modification of this file should be mirrored in  $(WEBROOT)/s/configuration.php
# by calling config_mirror.py

#######################################
# choose debug mode, set to 0 when in production !
$DEBUG_MODE = 0;

#######################################
# name of the WEB site :
$WEBSITE = 'www2.netforgod.tv';
#######################################
# addres and set-up for the programs
# address of the prgm directory, which contains all the scripts
#export MAKEdir=/Library/WebServer/Documents/NFG/FOI_prgm
$MAKEdir = '/home/netforgod/FOI_prgm';


#######################################
# address for the main web site
# address of the WEB folders, some file have to be at this level.
#export WEBROOT=/Library/WebServer/Documents/NFG
$WEBROOT = '/home/netforgod/www';

# address of the VIDEO directory which contains the genuine content
# this dir is not public
#export VIDEOdir=/Library/WebServer/Documents/NFG/videos
$VIDEOdir = '/home/netforgod/www/videos';

# address of the VOD directory : contains flv and other VOD material
#export VODdir=/Library/WebServer/Documents/NFG/VOD
$VODdir = '/home/netforgod/www/VOD';


#######################################
# commands for coders
# FFMPEG command - usually prefixed with nice
#export FFMPEG=echo
$FFMPEG = 'nice /home/netforgod/USR/bin/ffmpeg';
#-benchmark

#######################################
# general parameters
# copyright notice (for meta information)
$COPYRIGHT = 'NetForGod';

#film price - not used so far.
$film_price = 10.00;

########################################
?>
