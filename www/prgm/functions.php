<?php
# fonctions et initialisation

// Ce fichier ne sera execute qu'une fois

include_once("configuration.php");

####################################################################################
#initialisation des variables globales
#dossier de base
#$basedir="/var/www";   # sans / à la fin

#addresse sur le disque des programmes
$baseprgm=$MAKEdir;
#nom du fichier de lock qui bloque le pipeline
$FOIlock="$MAKEdir/FOI-blocked.lock";

#addresse sur le disque de sources video
$basevideos=$VIDEOdir;

#addresse sur le disque de VOD
$basevod=$VODdir;

#addresse sur le disque de DIVX
#$basedivx="$basedir/FOI";

#base de l'URL des VOD
$urlvod="/VOD";
#base de l'URL des DIVX
#$urldivx="/FOI";

#liste des video de type VOD/FOI_xx_xx, déjà triée
$list_video=array();
$list_FOI=array();
$myDir = opendir($basevideos);
    while($file = readdir($myDir)) {
        if (is_dir("$basevideos/$file")) {
            if (!ereg("^\.",$file)) { $list_video[]=$file; }
            if (ereg("^FOI_.._..$",$file)) { $list_FOI[]=$file; }
        }
    }
sort($list_video);
sort($list_FOI);

$bavard = TRUE;

# nom de la video du mois
$video_du_mois="none";
@$video_du_mois=basename(readlink("$basedivx/download"));

$utilisateurs=array("public","netforgod", "admin", "temporaire");

$utils_flags=array(1 => "public", 2 => "netforgod", 4 => "administrateur", 8 => "temporaire");

# la commande qui recalcule la VOD
$calcul_vod = "python $baseprgm/do_vod.py";

# la commande qui recalcule la page de telechargement
$calcul_tele = "python $baseprgm/do_tele.py";

# la commande qui relance le make all
#$calcul_makeall = "pwd; ./auto.sh";
$calcul_makeall = "if ! [ -f FOI-working.lock ]; then touch FOI-working.lock; make  -C $basevideos  -f $baseprgm/Makefile  all; python do_vod.py; rm FOI-working.lock; else echo XX un calcul est deja actif XX; fi";

# utilitaire pour les url cod'es

###################################liste de fonctions

function list_video()   {
    # la liste des videos
    global $list_video;
    return $list_video;
}
function list_FOI()   {
    # la liste des videos de type FOI_YY_MM
    global $list_FOI;
    return $list_FOI;
}
function video_du_mois()    {
    # la video du mois
    global $video_du_mois;
    return $video_du_mois;
}

function list_divx($video) {
    # retourne la liste des divx pour une video
    global $list_FOI,$basevideos;
    $myDir = opendir("$basevideos/$video");
    $list_divx=array();
    while($file = readdir($myDir)) {
       if (ereg("divx.avi", $file)) { $list_divx[]=$file;}
    }
    sort($list_divx);
    return $list_divx;
}

function list_flv($video) {
    # retourne la liste des flv pour une video
    global $list_FOI,$basevideos;
    if (is_dir("$basevideos/$video")) {
        $myDir = opendir("$basevideos/$video");
        $list_flv=array();
        while($file = readdir($myDir)) {
           if (ereg("divx.flv$", $file)) { $list_flv[]=$file; }
        }
        sort($list_flv);        
    } else {
        $list_flv = "";
    }
    return $list_flv;
}

function titre($video)  {
    # retourne le titre en français d'une video
    global $basevideos;
    @$FTITRE = file_get_contents("$basevideos/$video/textes/titre_FR.txt");
    if (! $FTITRE) {
        $FTITRE = "<i>sans titre</i>";
    }
    return $FTITRE;
}
function titre_fr($video)  { return titre($video); }

function titre_en($video)  {
    # retourne le titre en anglais d'une video
    global $basevideos;
    @$FTITRE = file_get_contents("$basevideos/$video/textes/titre_EN.txt");
    if (! $FTITRE) {
        $FTITRE = "<i>no title</i>";
    }
    return $FTITRE;
}

function affiche($video) {
    # retourne l'url de l'affiche
    global $urlvod, $basevideos;
    if (file_exists("$basevideos/$video/affiche.jpg")) {
        return "$urlvod/$video/affiche.jpg";
    } else {
        return "/images/affiche.gif";
    }
}

function click($video)  {
    # transforme le nom d'une video en chaine cliquable
    global $urldivx;
    return "<a href=\"$urldivx/$video\">$video</a>";
}

function click_blank($video)  {
    # transforme le nom d'une video en chaine cliquable dans une nouvelle fenetre
    global $urldivx;
    return "<a href=\"$urldivx/$video\" target=\"_blank\">$video</a>";
}

function est_cachee($video) {
    # vraie si la video est cach�e dans la liste VOD
    global $basevideos;
    return (! file_exists("$basevideos/$video/public"));
}

function est_premier($video) {
    # vraie si la video est premier dans la liste VOD
    global $basevideos;
    if (!est_cachee($video)) {
        return (file_exists("$basevideos/$video/premier"));
    } else {
        return False;
    }
}

function cont($message) {
    # pour arreter une page
    echo "<center>";
    echo "<H2>Traitement réalisé</H2>";
    echo "<H3>$message</H3>";
    echo '<P><a href="index.php"> Cliquez ici pour continuer</A></P>';
    echo "</center>";
    echo '</body></html>';
    exit();
}

function arret($message) {
    # pour arreter et faire un message d'erreur
    echo "<center>";
    echo "<H1>Erreur dans le traitement</H1>";
    echo "<H2>$message</H2>";
    echo '<P><a href="index.php"> Cliquez ici pour continuer</A></P>';
    echo "</center>";
    echo '</body></html>';
    exit();
}

function perm_dir($dir) {
    # retourne un tableau qui contient la liste des utilisateurs permis (dans le fichiers .htacces) pour un dir
    # suppose un .htpasswd local
    $trouve=array();
    $passwd="$dir/.htpasswd";
    $access = "$dir/.htaccess";
    $ok_access = file_exists($htaccess);
    $ok_pass = file_exists($pass);
    if (file_exists($htaccess)) {
         $htaccess = file_get_contents($access);
        }
$handle = @fopen("/tmp/inputfile.txt", "r");
if ($handle) {
    while (!feof($handle)) {
        $buffer = fgets($handle, 4096);
        echo $buffer;
    }
    fclose($handle);
}
    }

        if (file_exists($fichier)){ # code dans htpasswd et htaccess

    } else { if (! file_exists($htaccess)) {
    } else {
    }
}

function perm_video($video) {
    # retourne un tableau qui contient la liste des utilisateurs permis (dans le fichiers .htacces) pour une video
    global $basedir,$utils_flags;
    $fichier="$basedivx/.htaccess";
    if (! file_exists($fichier)){
        $val = array("public");
    } else {
        $htaccess = file_get_contents($fichier);
        $trouve=array();
        foreach ($utils_flags as $key => $val) {      # pour tout les utilisatuers
            if (preg_match("/$val/", $htaccess)) {  # cherche le nom
                $trouve[]=$val;
            }
        }
        $val = $htaccess;
    }
    return $val;
}

function travail_en_cours() {
    # retourne vrai si un calcul est en cours
    # plus pr�cis�ment, la dur�e en secondes depuis le lancement du calcul
    global $baseprgm;
    $lock = "$baseprgm/FOI-working.lock";
    if (file_exists($lock)) {
        $dur=time() - filectime($lock);
        if ($dur==0) {$dur=1;}
        return $dur;
    } else {
        return 0;
    }
}

function travail_bloque() {
    # retourne 1 si le pipe-line de calcul est bloqu�
    global $FOIlock;
    if (file_exists($FOIlock)) {
        return 1;
    } else {
        return 0;
    }
}
function makelog($text) {
    # rajoute une entrée dans le log file
    global $baseprgm;
    system ("(echo \"######## Calcul lance depuis l interface WEB ########\";echo $text;date) >>".$baseprgm."/make.log" );
}
