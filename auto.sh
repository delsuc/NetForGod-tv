#!/bin/sh
# ce script est appele par cron regulierement

# on commence par dater dans le log
echo "################## "
date
w

# import the configuration
. configuration.sh

if [ -f FOI-blocked.lock ]; then echo calcul bloque volontairement;
  echo le fichier FOI-blocked.lock doit etre retire manuellement;
  exit;
fi

# ouvre les fichiers de VOD
#chmod -R a+w $VODdir/*

# enleve les vieux fichiers non utilises
./clean.sh

# fabrique tous les fichiers video et les fichiers html
if ! [ -f FOI-working.lock ]; then touch FOI-working.lock; 
   make -s  -C $VIDEOdir  -f $PWD/Makefile  all;
   python do_vod.py
   rm FOI-working.lock;
else 
  echo "calcul deja actif (FOI-working.lock)";
fi

# pour le faire a la main
# i) verifier que rien ne tourne sur le serveur (via le back office) / page Outils 
# ii) taper la commande : (-n montre seulement , ne fait rien enlever -n pour le faire)
# make -s -w -n -C /var/www/videos  -f $PWD/Makefile  all;
# iii) reactiver dans Outils
