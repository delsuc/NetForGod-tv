www-data@nfg1:~$ cat VOD/perm.php
<?php
function titre($video)  {
    # retourne le titre en français d'une video
    global $basevideos;
    @$FTITRE = file_get_contents("$basevideos/$video/textes/titre_FR.txt");
    if (! $FTITRE) {
        $FTITRE = "<i>sans titre</i>";
    }
    return $FTITRE;
}

# bases
$basevideos = "../videos";    # base pour file system
$baseVOD = "../VOD";  # base pour file system
$urlVOD = "/VOD";  # base pour URL

# GET
#$dt = "10_05";
@$dt = $_GET["dt"];
#$lg = "EN";
@$lg = $_GET["lg"];

$video = "FOI_$dt";

$ok = file_exists("$baseVOD/${video}/${lg}_divx.flv") & file_exists("$basevideos/${video}/public");

if (! $ok) {    # someting is wrong
    $title = "Erreur";
    $titlehtml = "Erreur";
} else {
    # files and url
    #$film = "/VOD/FOI_10_05/FR_divx.flv";
    $film = "$urlVOD/${video}/${lg}_divx.flv";
    $affiche = "$urlVOD/${video}/affiche.jpg";
    $title = titre($video);
    $titlehtml = ereg_replace("\n","<br/>",$title);
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<title> <?php echo $title;?> </title>
<link href="/nfg.css" type="text/css" media="screen" rel="stylesheet">
<link rel="shortcut icon" type="image/x-icon" href="/images/favicon.ico">
<script type="text/javascript" src="/js/swfobject.js"></script>
<script language="JavaScript">
<!--
function openWindow(url,name)
{ popupWin = window.open(url,name,'resizable, scrollbars, width=850,height=300')
}
function CalLangue(){
	var vid = "<?php echo $film;?>";
	var aff = "<?php echo $affiche;?>";
	//var s1 = new SWFObject("../jw_flvplayer.swf","single","352","287","7");
	var s1 = new SWFObject("jw_flvplayer.swf","single","558","420","7");
	s1.addParam("allowfullscreen","true");
	s1.addVariable("file",vid);
	s1.addVariable("image",aff);
	s1.addVariable("width","558");
	s1.addVariable("height","420");
	//s1.addVariable("width","352");
	//s1.addVariable("height","287");
	s1.addVariable('frontcolor','0x5f6486');
	s1.addVariable('lightcolor','0xFFFFFF');
	s1.addVariable('backcolor','0x000000');
	s1.write("video_sa");
}
// -->
</script>
</head>
<body onload="CalLangue()">
<a href="/"><img id="logo" border="0" src="/images/logo_FOI.gif" alt="Logo" border="0" title="Réseau NetForGod"></a>
<img id="header" src="/images/bande-800-s.jpg" alt="header">

<div id="bandeau">
<div class="bd-gauche">
 <a id="ccn" href="http://www.chemin-neuf.org"><img src="/images/logo_k4.gif" height="35" border="0" alt="Logo Communaute du Chemin-neuf" title="Communauté du Chemin-Neuf"></a>
        Au service de l'UNITÉ des CHRÉTIENS et de la PAIX dans le MONDE. 
    </div>
    <div class="bd-droit">    Français<a href="permn.php?<?php echo "dt=$dt&lg=EN";?>"> / English</a>    </div>
</div>
<div id="page-centree" style="font-size: 16px">

<?php
# error page
if (! $ok) {    # someting is wrong
?>

<h1>IL Y A UN PROBLEME !!!!</h1>
<p>Veuillez revenir dans qq instant</p>

<?php
} else {    # everything seems ok
# le nom des langues en français
$langues = array('FR'=>'Français', 'EN'=>'Anglais', 'DE'=>'Allemand', 'ES'=>'Espagnol', 'IT'=>'Italien','PT'=>'Portugais',
        'HU'=>'Hongrois','NL'=>'Néerlandais','CS'=>'Tchèque','SK'=>'Slovaque','LV'=>'Letton','PL'=>'Polonais','RU'=>'Russe', 'LT'=>'Lituanien',
        'TR'=>'Turc', 'AR'=>'Arabe','HY'=>'Arménien','ZH'=>'Chinois','JA'=>'Japonais','VI'=>'Vietnamien',
        'MOS'=>'Mooré','LN'=>'Lingala','RN'=>'Kirundi','MU'=>'Créole Mauricien','MG'=>'Malgache');
# le nom des langues en anglais
$languages = array('FR'=>'French', 'EN'=>'English', 'DE'=>'German', 'ES'=>'Spanish','IT'=>'Italian','PT'=>'Portuguese',
        'HU'=>'Hungarian','NL'=>'Dutch','CS'=>'Czech','SK'=>'Solvak','LV'=>'Latvian','PL'=>'Polish','RU'=>'Russian', 'LT'=>'Lithuanian',
        'TR'=>'Turkish','AR'=>'Arabic','HY'=>'Armenian','ZH'=>'Chinese','JA'=>'Japanese','VI'=>'Vietnamese',
        'MOS'=>'Mossi','LN'=>'Lingala','RN'=>'Kirundi','MU'=>'Mauritian Creole','MG'=>'Malagasy');

# le nom des langues dans leur propres langue
$lang_self = array('FR'=>'Français', 'EN'=>'English', 'DE'=>'Deutsch', 'ES'=>'Español','IT'=>'Italiano','PT'=>'Português',
        'HU'=>'Magyar','NL'=>'Nederlands','CS'=>'Česky','SK'=>'Slovenčina','LV'=>'Latviski','PL'=>'Polski','RU'=>'Pусский', 'LT'=>'Lietuviškai',
        'TR'=>'Türkçe','AR'=>'العربية','HY'=>'Հայերեն','ZH'=>'漢語','JA'=>'日本語','VI'=>'Tiếng Việt',
        'MOS'=>'Mòoré','LN'=>'Lingala','RN'=>'Kirundi','MU'=>'Kreol moricien','MG'=>'Malagasy');

$ordrelangues = array('FR','EN','DE','ES','IT','PT','HU','NL','CS','SK','LV','LT','PL','RU','TR','HY','AR','ZH','JA','VI','MOS','LN','RN','MU','MG');   # rajouter les nouvelles langues à la fin
$availl = array(); # get all available language
foreach ($ordrelangues as $l){
    if (file_exists("$baseVOD/${video}/${l}_divx.flv")) { $availl[] = $l;}
    }

?>


<p class="titre-mois"> <?php echo "$titlehtml";?> <br/></p>


<div id="video_sa">
		<img src="http://www.adobe.com/images/icons/alert.gif" alt="Alert" height="16" width="16"/>Cette page nécessite Flash
		<p class="titre-mois">Pour voir ce contenu, Javascript doit être activé
et vous télécharger Adobe Flash Player .</p>
		<p class="titre-mois"><a href="http://get.adobe.com/fr/flashplayer" target="_top">
Télécharger maintenant!</a></p>
		<a href="http://get.adobe.com/fr/flashplayer" class="noHover" target="_top"><img src="http://www.adobe.com/images/shared/download_buttons/get_flash_player.gif" alt="Get Adobe Flash Player" border="0" height="33" width="112"/></a>
</div>

<div class="langues_sa">

<p><span class="Blangue"> <?php echo $lang_self[$lg]; ?></span>
<br/>- <a href="javascript:openWindow('resume.php?c=FOI_10_10&l=<?php echo $lg;?>&d=FR')"> Résumé </a> - </p>
<!-- <p> EMBED : <input type="text" name="embed" with="30" value="" id="some_name"/></p> -->
<p>choisissez une autre langue:</p>
<p>
<?php 
    foreach ($availl as $l) {
        if ($l == $lg) {
            echo "- $lang_self[$l] \n";            
        } else {
            echo "- <a href=\"perm.php?dt=$dt&lg=$l\" title=\"$lang_self[$l]\">$langues[$l]</a>\n";
        }
    }
?>
- </p>
<hr width="60%">
<a style="font-size: 16px" href="liste.html">liste des autres films</a> <br>
<hr width="60%">
<p class="diapo">
<a style="font-size: 16px" href="/frat.html">Découvir la fraternité NetForGod</A> <br>
<hr width="60%">
</div>

<BR CLEAR=ALL>
<div id="pied">
<ul>
<li><a href="copyright.html">&copy; C.C.N.</a></li>
<li>| <a href="http://chemin-neuf.org">La communaut&eacute; du Chemin-Neuf </a> | </li>

<li><a href="/mentions.html">mentions l&eacute;gales</a> | </li>
<li><a href="mailto:netforgod@chemin-neuf.org?cc=nfg.webmaster@gmail.com&subject=depuis le site netforgod.tv" >contactez-nous</a> | </li>
<li>Ce site est optimis&eacute; pour Firefox</li>
</ul></div></div></div>
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-4576934-2");
pageTracker._initData();
pageTracker._trackPageview();
</script>
</body></html>
<?php } # else (no problem) ?>
www-data@nfg1:~$ 
