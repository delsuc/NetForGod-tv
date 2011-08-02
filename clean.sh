# pour faire de la place sur le disque.
active="False"

. configuration.sh

# le dir ou on fait de la place
depot=$VIDEOdir

# le delai en jours ou on garde les fichiers
delai="+100"

# liste de toutes les videos non lues depuis un certain temps
echo "find $depot -name "*_divx.avi" -not -name FR_divx.avi -not -name EN_divx.avi -not -empty -atime $delai"
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
