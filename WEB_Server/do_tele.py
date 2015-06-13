#X!/usr/bin/python
# -*- coding: utf-8 -*-
""" pour faire la page d'index du mois"""

import re
import os
import sys
import langues
import FOIlib
import traceback


debug=0  # mettre à 1 pour debugger, le nom des fichiers de sortie est changé et le prgm donne des info

# definition du directory ou se fait le travail
# la valeur est effacée au lancement par argv[0]
global current_dir, page, page_wrong
current_dir = './'

# page template for download
page="""<!DOCTYPE html">
<html lang="en,fr" xml:lang="en,fr" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<meta content="NetForGod page " name="description" />
<title> Téléchargement de vidéo Net for God</title>
<STYLE TYPE="text/css"> a { text-decoration: none} </STYLE>
<link rel="shortcut icon" type="image/x-icon" href="/images/favicon.ico" />
</head>
<body bgcolor="#000000" text="#FFFFCC"  link="#FF0033" style="font-size:12pt; font-family: verdana,sans-serif; color=#FFFFCC">
<div style="margin-left:auto; margin-right:auto; text-align:center;">
<IMG alt="banner" src="/images/banner_yellow.jpg" border="0" width="800">
<P><span style="font-size:18pt";>Fraternité Œcumenique Internationale</span><br/>
Bienvenue sur la page de téléchargement de vidéo </P>
<hr width="30%%">
<P><i> <span style="font-size:18pt";>International Ecumenical Fraternity </span><br/>
Welcome to the video downloading page</i> </p>
<div style="width:600px; margin-left:auto; margin-right:auto; text-align:center;">
<hr width="100%%">
<p> %(mois_st)s - <i>%(month_st)s</i> - %(an)i </p>
<p> <b>%(titre)s</b></p>
<p><i><b>%(title)s</b></i></p>
<IMG alt="affiche" src="%(affiche)s" border="0" width="320" height="240">
<hr width="30%%">
%(opt_st)s
<p>cliquez sur la langue choisie, et le t&eacute;l&eacute;chargement commence<br/> (il peut y avoir un délai de quelques secondes)</p>
<P><i>click on the chosen language, and the download will start<br/> (a delay of a few seconds is possible)</i></p>
<hr width="30%%">
<p style="font-size:14pt;">
%(list_langues)s - </p>
<p style="font-size:10pt; color:#888888">
- %(duree)i minutes - %(taille)i Mo AVI format, DivX codec -<br/> 
- Temps de téléchargement estimé - <i>Estimated download time :</i> -<br/>
<span id="temp_load">
<img src="/images/loading.gif" width="16" height="16" />
computing ...
</span>
<span id="calc_load"></span>
</p>
<hr width="30%%">
</div>
<li><a href="http://www.netforgod.tv" target="_blank">Voir les autres films en ligne</A></li>
<li><i><a href="http://www.netforgod.tv/VOD/index_en.html" target="_blank">Watch the other movies online</a></i></li>
<hr width="30%%">
<p><a href="../conseils.html" target="_blank">Quelques conseils</a> pour regarder ce film<br/>
<i><a href="../advices.html" target="_blank">Some advice</a> to watch this film</i></P>
<hr width="100%%">
</div>
<p style="text-align:center"> FRATERNITÉ ŒCUMÉNIQUE INTERNATIONALE - - NET FOR GOD - - INTERNATIONAL ECUMENICAL FRATERNITY </p>
<?php
// speed-test from http://jan.moesen.nu/code/php/speedtest/index.php
function getmicrotime()
{    list($usec, $sec) = explode(" ", microtime());    return ((float)$usec + (float)$sec);}
$numKB=1000;
flush();
$nlLength = strlen("\n");
echo "<!--";
$timeStart = getmicrotime();
for ($i = 0; $i < $numKB; $i++)
{    echo str_pad('', 1024 - $nlLength, '/*\\*') . "\n";   flush(); }
$timeEnd = getmicrotime();
$timeDiff = $timeEnd - $timeStart;
echo "-->";
$thisline = 8*$numKB / $timeDiff;       // debit e'stime' de la ligne
$timedowload = round( %(taille)i *1024*10/$thisline/60);
$load_html = "$timedowload minutes.<br/>";
if ($timedowload>60) {
        $load_html = $load_html."WARNING, the downlaod time is over one hour, risks of failure are important.<br/>";
        }
elseif ($timedowload>30) {
         $load_html = $load_html."Warning, download time is over 30 minutes.<br/>";
        }
if ($timedowload>30) {
         $load_html = $load_html."Insure that the line is stable during download, or consider downloading from a faster line. ";
}
?>
<script type="text/javascript">
var d = document.getElementById("temp_load");
d.style.display='none';
var dl = document.getElementById("calc_load");
dl.innerHTML=" <?php echo $load_html; ?> ";
</script>
</div>
</body>
</html>
"""

# page if something went wrong
page_wrong="""<!DOCTYPE html">
<html lang="en,fr" xml:lang="en,fr" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<meta content="NetForGod page " name="description" />
<title> Téléchargement de vidéo Net for God</title>
<STYLE TYPE="text/css"> a { text-decoration: none} </STYLE>
<link rel="shortcut icon" type="image/x-icon" href="/images/favicon.ico" />
</head>
<body bgcolor="#000000" text="#FFFFCC"  link="#FF0033" style="font-size:12pt; font-family: verdana,sans-serif; color=#FFFFCC">
<div style="margin-left:auto; margin-right:auto; text-align:center;">
<IMG alt="banner" src="/images/banner_yellow.jpg" border="0" width="800">
<P><span style="font-size:18pt";>Fraternité Œcumenique Internationale</span><br/>
Bienvenue sur la page de téléchargement de vidéo </P>
<hr width="30%">
<P><i> <span style="font-size:18pt";>International Ecumenical Fraternity </span><br/>
Welcome to the video downloading page</i> </p>
<div style="width:600px; margin-left:auto; margin-right:auto; text-align:center;">
<hr width="100%">
<H1>Pas de téléchargement disponible pour le moment.</H1>
<H1><I>No download available for the moment.</I></H1>
<hr width="100%">
</div>
<p style="text-align:center"> FRATERNITÉ ŒCUMÉNIQUE INTERNATIONALE - - NET FOR GOD - - INTERNATIONAL ECUMENICAL FRATERNITY </p>
</div>
</body>
</html>
"""

def html(fichier):
    """ fabrique le fichier index.html"""
    global current_dir, page, page_wrong
    (an,mois)=FOIlib.current_date(current_dir)
    try:
        taille = os.stat(os.path.join(current_dir,'FR_divx.avi')).st_size/1024/1024
        debit = 1100;                                      # debit en kbit/sec
        duree = taille*1024*8/debit/60       # durée du film
        (titre,title)=FOIlib.current_title(current_dir)
        titre = "<BR/>".join(titre)
        title = "<BR/>".join(title)
        try:
            affiche=os.path.join(current_dir,'affiche.jpg')
            f=open(affiche)
            f.close()
            affiche='affiche.jpg'
        except:
            affiche='/images/affiche.gif'
        mois_st = langues.mois_nom[mois]
        month_st = langues.month_name[mois]
        optional = 0
        opt_st = ''
        if os.path.exists(os.path.join(current_dir,"diaporama_FR.html")):
            opt_st = opt_st+'<a href="diaporama_FR.html">Diaporama</A>\n'
            optional=optional+1
        if optional:
            opt_st = opt_st + '<hr width="30%%">\n'
        list_divx=FOIlib.read_dir(current_dir,"*")
        list_langues = ""
        for ll in langues.ordrelangues.split():
            for divx in list_divx:
                nom_d=os.path.basename(divx)
                if nom_d.startswith(ll):
                    tele="dl.php?lang=%s&date=%s%d"%(ll,langues.mois_nom_court[mois],an)
                    list_langues += """ - <a href="%s" title="%s - %s">[%s]</a> """%(tele, langues.langues[ll], langues.languages[ll], langues.lang_self[ll])
                    break
        fichier.writelines(page%vars())
    except: # something went wrong
        print traceback.print_exc()
        fichier.writelines(page_wrong)
        
def push_php():
    code = """<?  
// Basile HODARA - Juin 2007
// pour Net for God : WEB Download
// MAD oct 07 - rajout de set_time_limit
// MAD nov 07 - rajout du log et de file_tele
// MAD dec 08 - rajout de la creation du fichier au vol si taille == 0
// MAD jan 09 - adapted to PEAR

// based on PEAR:HTTP:Download - allows restart
include_once( 'HTTP/Download.php');

// récupération du fichier à télécharger
$lang=$_GET['lang'];
$date=$_GET['date'];
$file=$lang."_divx.avi";
$file_tele="FOI_".$date.$lang.".avi";
$stat="dl.log";
if (file_exists($file)) {
    @$taille=filesize("$file" );
    if ($taille == 0) {  // means just a template is left, we need to rebuild it
        $cmd = "/var/www/prgm/do_mux.sh video.avi sons/$lang.mp3 $file";    // to be adapted to your local set-up
        system($cmd);
        system("touch $lang"."_divx.flv"); // to hamper automatic computation
        $taille=filesize("FR_divx.avi"); // for some reason filesize($file) gives 0
    }
    // open log file
    $curdate=date("[d/M/Y:H:i:s O]");
    $IP=$_SERVER['REMOTE_ADDR'];
    $AGENT=$_SERVER['HTTP_USER_AGENT'];
    $SCRIPT=$_SERVER['SCRIPT_NAME'];

    @$F=fopen($stat,"a");
    @fputs($F,"$IP - - $curdate \\"BEGIN $lang\\" 200 0 \\"$SCRIPT\\" \\"$AGENT\\"\n");
    @fclose($F);

    // forçage du téléchargement  
    set_time_limit(120);
    $params = array(
       'file'                => $file,
       'contenttype'         => 'video/avi',
       'contentdisposition'  => array(HTTP_DOWNLOAD_ATTACHMENT, $file_tele),
      );
    $error = HTTP_Download::staticSend($params, false);
    $curdate=date("[d/M/Y:H:i:s O]");
    @$F=fopen($stat,"a");
    @fputs($F,"$IP - - $curdate \\"END $lang\\" 200 $error \\"$SCRIPT\\" \\"$AGENT\\"\n");
    @fclose($F);
} else {
?>
<!DOCTYPE html">
<html lang="en,fr" xml:lang="en,fr" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<meta content="NetForGod page " name="description" />
<title> Error</title>
<STYLE TYPE="text/css"> a { text-decoration: none} </STYLE>
<link rel="shortcut icon" type="image/x-icon" href="/images/favicon.ico" />
</head>
<body bgcolor="#000000" text="#FFFFCC"  link="#FF0033" style="font-size:12pt; font-family: verdana,sans-serif; color=#FFFFCC">
<div style="margin-left:auto; margin-right:auto; text-align:center;">
<IMG alt="banner" src="/images/banner_yellow.jpg" border="0" width="800">
<H1>Erreur </H1>
<H1><I>Error</I></H1>
<P> <B><? echo $_GET['lang']; ?></B> :  Langue inconnue - <i>unsuported language</I></P>
<p> <? echo "$lang "; ?></P>
<P> Faire -retour- sur votre navigateur s'il vous plait</P>
<P> <I>Please hit -Back- on your browser</I></P>
</div> </body> </html>
<?
}
exit();  
?>
"""
    fout=open(os.path.join(current_dir,"dl.php"),'w')
    fout.writelines(code)
    fout.close()

def faire():
    if debug:
        fout=open(os.path.join(current_dir,"indexd.php"),'w')
    else:
        fout=open(os.path.join(current_dir,"index.php"),'w')
    html(fout)
    fout.close()
    push_php()

if __name__ == "__main__":
    try:
        c = sys.argv[1]
    except:
        print """\
La syntaxe normale est :
python do_tele.py video_dir

le programme construit la page dans video_dir
"""    
        c="."
    current_dir = c
    FOIlib.current_title(c)
    faire()


