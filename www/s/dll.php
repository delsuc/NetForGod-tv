<?php
include_once( '../prgm/configuration.php');
include_once("../prgm/langues.php");
include_once("../prgm/codec.php");
include_once("../prgm/functions.php");

@$debug=$_GET['d'];
@$code=$_GET['c'];

$t = decodage($code);
$date = $t[0];
$video = $t[1];
$year = floor($video/100);
$month = $video % 100;
$lang = $t[2];
$foi = sprintf("FOI_%02d_%02d",$year,$month);
$dir = sprintf("$VIDEOdir/FOI_%02d_%02d",$year,$month);
$cmd = "$MAKEdir/do_mux.sh $dir/video.avi $dir/sons/$lang.mp3 $film";    // to be adapted to your local set-up

$tt = file_exists("$dir/FR_divx.avi");
# verif les erreur
$erreur = '';
if ($date*3600 < time()) {
    $erreur = "lien périmé - <i>Link is too old.</i>";
}
if (! $tt) {
    $erreur = "Lien inactif - <i>inactive link</i>";
}

if ($debug != '' ){
    echo "<hr/>";
    printf("film : $foi<br/>");
    printf("fichier à telecharger : $file_tele<br/>");
    $valid = getdate($date*3600);
    echo "date de validité : $valid[mday] $valid[mon] $valid[year]<br/>";
    $valid = getdate(time());
    echo "aujourd'hui : $valid[mday] $valid[mon] $valid[year]<br/>";
    echo "$erreur<br/>";
    echo "<hr/>";
}

if ($erreur == ''){
    $taille = filesize("$dir/FR_divx.avi")/1024/1024;
    $debit = 1100;                                      # debit en kbit/sec
    $duree = $taille*1024*8/$debit/60;       # durée du film

    if ($debug != '' ){
        echo "taille du fichier $taille Mo<br/>";
        echo "duree du film : $duree mn<br/>";
    }
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en,fr" xml:lang="en,fr" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<meta content="NetForGod page " name="description" />
<title> Téléchargement de vidéo Net for God</title>
<style TYPE="text/css"> a { text-decoration: none} </style>
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
<p> <?php echo $mois_nom[$month]; ?> - <i> <?php echo $month_name[$month]; ?></i> - <?php echo $year+2000; ?> </p>
<p> <b>﻿
    <?php echo titre_fr($foi); ?>
    </b></p>
<p><i><b>
    <?php echo titre_en($foi) ?>
</b></i></p>
<IMG alt="affiche" src="<?php echo affiche($foi) ?>" border="0" width="320" height="240">
<hr width="30%">

<p>cliquez sur la langue choisie, et le t&eacute;l&eacute;chargement commence<br/>
(il peut y avoir un délai de quelques secondes)</p>
<P><i>click on the chosen language, and the download will start<br/> (a delay of a few seconds is possible)</i></p>
<hr width="30%">
<p style="font-size:14pt;">
<?php
$date = time() + 3600*24*7;  # 7 days
foreach ($ordrelangues as $lang) {
    $film = "$dir/$lang"."_divx.avi";
    if (file_exists($film)) {
        $c = codage($date, $video, $lang) ;
        $self = $lang_self[$lang];
        $en = $languages[$lang];
        $fr = $langues[$lang];
        echo "- <a href=\"dl.php?c=$c\" title=\"$fr - $en\">[$self]</a>\n";
    }
}
?>
 - </p>
<p style="font-size:10pt; color:#888888">
- <?php echo (int) $duree ?> minutes - <?php echo (int) $taille ?> Mo AVI format, DivX codec -<br/> 
- Temps de téléchargement estimé - <i>Estimated download time :</i> -<br/>
<span id="temp_load">
<img src="/images/loading.gif" width="16" height="16" />
computing ...
</span>
<span id="calc_load"></span>
</p>
<hr width="30%">
</div>
<li><a href="http://<?php echo $WEBSITE; ?>" target="_blank">Voir les autres films en ligne</A></li>
<li><i><a href="http://<?php echo $WEBSITE; ?>/VOD/index_en.html" target="_blank">Watch the other movies online</a></i></li>
<hr width="30%">
<p><a href="/media/conseils.html" target="_blank">Quelques conseils</a> pour regarder ce film<br/>
<i><a href="/media/advices.html" target="_blank">Some advice</a> to watch this film</i></P>
<hr width="100%">
</div>
<p style="text-align:center"> FRATERNITÉ ŒCUMÉNIQUE INTERNATIONALE - - NET FOR GOD - - INTERNATIONAL ECUMENICAL FRATERNITY </p>
<?php
// speed-test from http://jan.moesen.nu/code/php/speedtest/index.php
$numKB=1000;
flush();
$nlLength = strlen(" 
");
echo "<!--";
$timeStart = getmicrotime();
for ($i = 0; $i < $numKB; $i++)
{    echo str_pad('', 1024 - $nlLength, '/*\*') . " 
";   flush(); }
$timeEnd = getmicrotime();
$timeDiff = $timeEnd - $timeStart;
echo "-->";
$thisline = 8*$numKB / $timeDiff;       // debit e'stime' de la ligne
$timedowload = round( $taille *1024*10/$thisline/60);
$load_html = "$timedowload minutes.<br/>";
if ($timedowload>60) {
        $load_html = $load_html."WARNING, the download time is over one hour, risks of failure are important.<br/>";
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
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-4576934-2");
pageTracker._initData();
pageTracker._trackPageview();
</script>
</body>
</html>
<?php
} else {            # if erreur
    sleep(5);
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
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
<H1>Erreur - <I>Error</I></H1>
<P> Erreur de Fichier - <i>File Error</I></P>
<p> - <?php echo $erreur ?> - </p>
<P> Vérifiez votre code s'il vous plait
- <I>Please verify your code</I></P>
</div> </body> </html>
<?
}
exit();  
?>
