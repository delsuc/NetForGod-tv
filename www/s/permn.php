<?php
include_once("../prgm/functions.php");
include_once("../prgm/langues.php");
$urlVOD = "/VOD";  # base pour URL

# GET
#$dt = "10_05";
@$dt = $_GET["dt"];
#$lg = "EN";
@$lg = $_GET["lg"];

$video = "FOI_$dt";

$ok = file_exists("$VODdir/${video}/${lg}_divx.flv") & est_public($video);

if (! $ok) {    # someting is wrong
    $title = "Error";
    $titlehtml = "Error";
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
<link href="/css/nfg.css" type="text/css" media="screen" rel="stylesheet">
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
<a href="/"><img id="logo" border="0" src="/images/logo_FOI.gif" alt="Logo" border="0" title="NetForGod Network"></a>
<img id="header" src="/images/bande-800-s.jpg" alt="header">

<div id="bandeau">
<div class="bd-gauche">
 <a id="ccn" href="http://www.chemin-neuf.org"><img src="/images/logo_k4.gif" height="35" border="0" alt="Logo Communaute du Chemin-neuf" title="Communauté du Chemin-Neuf"></a>
Working for Christian unity and for peace in the world ! 
    </div>
    <div class="bd-droit">
        English <a href="perm.php?<?php echo "dt=$dt&lg=FR";?>" class="faded">/ Français</a>
    </div>
<div id="page-centree" style="font-size: 16px">

<?php
# error page
if (! $ok) {    # someting is wrong
?>

<H1>There is a problem</H1>
<p>Please come backin a few minutes</p>
<?php
} else {    # everything seems ok
$availl = array(); # get all available language
foreach ($ordrelangues as $l){
    if (file_exists("$basevod/${video}/${l}_divx.flv")) { $availl[] = $l;}
    }

?>
<p class="titre-mois"> <?php echo "$titlehtml ";?> <br/></p>
<div id="video_sa">
	<img src="http://www.adobe.com/images/icons/alert.gif" alt="Alert" height="16" width="16"/>This content requires Flash
	<p class="titre-mois">To view this content, JavaScript must be enabled, and you need the latest version of the Adobe Flash Player.</p>
	<p class="titre-mois"><a href="http://www.adobe.com/go/getflashplayer" target="_top">Download the free Flash Player now!</a></p>
	<a href="http://www.adobe.com/go/getflashplayer" class="noHover" target="_top"><img src="http://www.adobe.com/images/shared/download_buttons/get_flash_player.gif" alt="Get Adobe Flash Player" border="0" height="33" width="112"></a>
</div>

<div class="langues_sa">

<p><span class="Blangue"> <?php echo $lang_self[$lg]; ?></span>
<br/>- <a href="javascript:openWindow('resume.php?<?php echo "c=$video&l=$lg&d=EN";?>')"> Summary </a> - </p>
<!-- <p> EMBED : <input type="text" name="embed" with="30" value="" id="some_name"/></p> -->
<p>choose another language :</p>
<p>
<?php 
    foreach ($availl as $l) {
        if ($l == $lg) {
            echo "- $lang_self[$l] \n";            
        } else {
            echo "- <a href=\"permn.php?dt=$dt&lg=$l\" title=\"$lang_self[$l]\">$languages[$l]</a>\n";
        }
    }
?>
- </p>
<hr width="60%">
<a style="font-size: 16px" href="/VOD/liste_en.html">list of all other movies</a> <br>
<hr width="60%">
<p class="diapo">
<a style="font-size: 16px" href="/frat.html">Discover the NetForGod fraternity</A> <br>
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
