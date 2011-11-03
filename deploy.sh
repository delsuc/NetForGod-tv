#!/bin/sh
echo "This scripts creates the required directories and copy the file into the live site" 
set -v on

. configuration.sh

# clean left-overs
./clean-up.sh

# create configuration.php from configuration.sh
python config_mirror.py

# create language utilities
python langues.py
# and copy over to work dir
mv langues.js www/js
mv langues.php www/prgm

# create directories
# first local for logs
mkdir -p logs

# first WEBROOT
mkdir -p $WEBROOT

# then subfolders
mkdir -p $VIDEOdir
mkdir -p $VODdir

# then utilities
for i in css js prgm s images; do
    mkdir -p $WEBROOT/$i
    cp www/$i/* $WEBROOT/$i
done

# create htaccess ref file
cat > htaccess_def <<EOF
AuthType Basic
AuthName "Acces reserve' aux membres $COPYRIGHT"
AuthUserFile $MAKEdir/.htpasswd
<limit GET PUT POST>
require valid-user
</limit>
EOF

# and copy to prgm folder
cp htaccess_def $WEBROOT/prgm/.htaccess

# PLEASE ENTER PASSWORD FOR WEB USER admin
htpasswd -c .htpasswd admin

# finally, instal crontab, but before save previous ones
crontab -l > previous_crontab
tail -n +2 crontab_eg | crontab -
#  currently installed crontab :
crontab -l

#=========================#
#=   deployement done    =#
#=========================#
