# This file contains all the configuration parameters for the FOI project

#######################################
# addres and set-up for the programs
# address of the prgm directory, which contains all the scripts
#export MAKEdir=/Users/mad/Desktop/NFG/prgm
export MAKEdir=/home/netforgod/prgm


#######################################
# address for the main web site
# address of the VIDEO directory which contains the genuine content
# this dir is not public
#export VIDEOdir=/Users/mad/Desktop/NFG/videos
export VIDEOdir=/home/netforgod/www/videos

# address of the VOD directory : contains flv and other VOD material
#export VODdir=/Users/mad/Desktop/NFG/VOD
export VODdir=/home/netforgod/www/VOD


#######################################
# commandes pour les codeurs
# addresse de FFMPEG
export FFMPEG="nice /home/netforgod/USR/bin/ffmpeg"
#-benchmark
#FFMPEG = echo

# la notice de copyright (apparait dans les meta informations)
export COPYRIGHT=NetForGod
