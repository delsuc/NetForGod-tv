#!/bin/sh
# ce script est appele par cron regulierement

#Configuration

MAKEdir=~/netforgod-tv/postproduction 
WORKdir=~/export

# on commence par dater dans le log
echo "##################"
date
w

cd $WORKdir
pwd

# enleve les liens casses
find -L . -lname "*" -print -delete

# fabrique tous les fichiers video et realise le transfert
if [ -f FOI-blocked.lock ]; then echo calcul bloque volntairement;
  echo le fichier FOI-blocked.lock doit etre retire manuellement;
  exit;
fi
if ! [ -f FOI-working.lock ]; then touch FOI-working.lock; 
   make -s -f $MAKEdir/Makefile  all;
   rm FOI-working.lock;
else 
  echo "calcul deja actif (fichier FOI-working.lock present)";
fi

