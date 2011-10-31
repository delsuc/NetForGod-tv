#!/bin/sh
# This scripts removed files which are created during set-up/configuration

. configuration.sh

set -v on
# clean left-overs
rm -f *.pyc langues.js www/js/langues.js langues.php 
# clean computed files
rm -f www/js/langues.js www/prgm/langues.php www/prgm/configuration.php
