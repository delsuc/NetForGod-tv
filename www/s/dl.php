<?  
// MAD oct 2009 - first version
// This prgm uses a crypted key (not very strong) to define a download link to a movie
// see in codec.php

//dl code base on plain dl put in each movie folder

// based on PEAR:HTTP:Download - allows restart

// uses a local version of pear install
set_include_path('/home/netforgod/pear/share/pear' . PATH_SEPARATOR  . get_include_path());
include_once( 'HTTP/Download.php');

include_once( '../prgm/configuration.php');
include_once( '../prgm/codec.php');
include_once( '../prgm/langues.php');

// récupération du fichier à télécharger
$code=$_GET['c'];
$debug=$_GET['d'];
$t = decodage($code);
$date = $t[0];
$video = $t[1];
$year = floor($video/100);
$month = $video % 100;
$lang = $t[2];
$dir = sprintf("$VIDEOdir/FOI_%02d_%02d",$year,$month);
$film = "$dir/$lang"."_divx.avi";
$stat = "$dir/dl.log";
#$file_tele=sprintf("FOI_%s_%02d_%02d.avi",$lang,$year,$month);
$file_tele=sprintf("FOI_%s20%02d_%s.avi",$mois_nom_court[$month], $year, $lang);
$cmd = "$MAKEdir/do_mux.sh $dir/video.avi $dir/sons/$lang.mp3 $film";    // to be adapted to your local set-up
$tt = file_exists($film);
# verif les erreur
$erreur = '';
if ($date*3600 < time()) {
    $erreur = "lien périmé - <i>Link is too old.</i>";
}
if (! $tt) {
    $erreur = "Lien inactif - <i>inactive link</i>";
}
# code de debug
if ($debug != '' ){
    echo "<hr/>";
    printf("film : $film<br/>");
    printf("fichier à telecharger : $file_tele<br/>");
    $valid = getdate($date*3600);
    echo "date de validité : $valid[mday] $valid[mon] $valid[year]<br/>";
    $valid = getdate(time());
    echo "aujourd'hui : $valid[mday] $valid[mon] $valid[year]<br/>";
    if ($date*3600 < time()) { echo "LIEN PERIME !<br/>";}
    echo "<hr/>";
    printf("log file : $stat<br/>");
    printf("validité : %06d<br/>",$date);
    echo "test existence : $tt<br/>";
    if (! $tt) { echo "LE FICHIER N EXISTE PAS<br/>";}
    echo "command : $cmd<br/>";
    echo "$erreur<br/>";
    exit();
}
# fait le travail
$file = $film;
if (! $erreur) {
    @$taille=filesize("$file" );
    if ($taille == 0) {     // means just a template is left, we need to rebuild it
        system($cmd);
        system("cd $dir; touch $lang"."_divx.flv"); // to hamper automatic computation
        $taille=filesize("$dir/FR_divx.avi"); // for some reason filesize($file) gives 0
    }
    // open log file
    $curdate=date("[d/M/Y:H:i:s O]");
    $IP=$_SERVER['REMOTE_ADDR'];
    $AGENT=$_SERVER['HTTP_USER_AGENT'];
    $SCRIPT=$_SERVER['SCRIPT_NAME']."?c=".$code;

    @$F=fopen($stat,"a");
    @fputs($F,"$IP - - $curdate \"BEGIN $lang\" 200 0 \"$SCRIPT\" \"$AGENT\"
" );
    @fclose($F);

    // forçage du téléchargement  
    set_time_limit(120);
    $params = array(
       'file'                => $file,
       'contenttype'         => 'video/avi',
       'contentdisposition'  => array(HTTP_DOWNLOAD_ATTACHMENT, $file_tele),
      );
    $erreur = HTTP_Download::staticSend($params, false);
    $curdate=date("[d/M/Y:H:i:s O]");
    @$F=fopen($stat,"a");
    @fputs($F,"$IP - - $curdate \"END $lang\" 200 $erreur \"$SCRIPT\" \"$AGENT\"
");
    @fclose($F);
} else {
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
