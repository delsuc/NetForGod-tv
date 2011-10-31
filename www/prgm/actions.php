<?php

# actions réalisées par les boutons dans les pages d'aministration

# recup parametre
@$action = $_GET["action"];
if ($action){
    if ($action == "Changer les droits") {
# Une vidéo est cachée ssi il n'y a pas un fichier nommé public dans le dossier => on unlink ou touch les fichiers en question.
# Une vidéo est en premier dans la liste si il y a un fichier nommé premier dans le dossier => on unlink ou touch les fichiers en question.
        if ($bavard) { echo"<p>Je fais le traitement des fichiers</p>"; }
	    foreach (list_video() as $file) {   # on parcourt la liste pour trouvée les visibles
            if ($bavard) {
    	        echo "<li>$file ";
                echo "$basevideos/$file/public";
                }
	        if ($_GET["premier"] == $file) {  # premier
    	        $F=fopen("$basevideos/$file/premier","w");
    	        fwrite($F,"fichier en tete");
    	        fclose($F);
    	        symlink("$basevod/$mois","$basevod/actuel" );
	        } else {
    	        @unlink("$basevideos/$file/premier");
	        }
	        if (isset($_GET[$file])) {  # visible
    	        $F=fopen("$basevideos/$file/public","w");
    	        fwrite($F,"fichier publique");
    	        fclose($F);
	        } else {
    	        @unlink("$basevideos/$file/public");
    	        @unlink("$basevideos/$file/premier");
	        }
            // if (! $ok) {
            //  arret("Il y a eut un problème avec cette opération pour $file.");
            // }
        }
        if ($bavard) {
            echo ("<p> Je fais le recalcule de la page</p><pre>"); 
            system($calcul_vod);     # ensuite on appelle python
            echo("</pre>");
            cont("c est fait !");
        } else {
            system($calcul_vod);
        }
    }
    elseif ($action == "Inverser l\'état") {
        if (file_exists($FOIlock)) {
            if ($bavard) {  echo ("<p> Pipeline inactif<br>Je le réactive</p>"); }
            unlink($FOIlock);
        } else {
            if ($bavard) {  echo ("<p> Pipeline actif<br>Je le déactive</p>"); }
	        $F=fopen($FOIlock,"w");
	        fwrite($F,"fichier lock");
	        fclose($F);
        }
    }
    elseif ($action == "Afficher les langues disponibles") {
        echo ("<p> Je fais le recalcul de la page"); 
        passthru("python langues.py");     # ensuite on appelle python
        cont("c est fait !");
    }
    else {
# fin des actions possibles
        arret("<I>$action</I> : action inconnue");
    }
	system("sleep 1");	# 1 sec de pause permettent la mise à jour
}



?>
