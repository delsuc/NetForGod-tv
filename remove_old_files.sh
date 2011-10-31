# remove all .avi files which can be recomputed rapidly from video.avi + langue/mp3
# FR and EN are always kept

# active can be "True" of "False" (in which case only a message is issued)
active="False"

. configuration.sh

# le dir ou on fait de la place
depot=$VIDEOdir

# le delai en jours ou on garde les fichiers
delai="+100"

# liste de toutes les videos non lues depuis un certain temps
l=`find $depot -name "*_divx.avi" -not -name FR_divx.avi -not -name EN_divx.avi -not -empty -atime $delai`

for i in $l; do
    if [ active == "True" ]; then
        echo "j enleve" $i
        # rm $i  # je l'enleve
        # touch $i   # je la recree vide
        # sleep 1
        # touch ${i/.avi/.flv}  # j'assure que le .flv soit maintenu
    else
        echo "je n enleve pas" $i
    fi
done
