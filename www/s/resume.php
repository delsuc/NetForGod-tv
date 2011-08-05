<?php
####################################################################################
# recup des arguments   m:mois  y:année   l:langue
@$lang = $_GET["l"];    # code de la langue 
@$deflang = $_GET["d"];    # code de la langue par défaut
@$code = $_GET["c"];    # code du film : FOI_YY_MM
# verifie les _GET
if ($deflang == "") {
	$deflang = "FR";
}
if ($lang == "AR") {    # Arabic is right to left.
	$dir = "rtl";
} else {
	$dir = "ltr";
}
# header
header("Content-Type: text/html; charset=UTF-8");
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="<?php echo $lang ?>" dir="<?php echo $dir ?>">
<head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8"/>
    <link rel="shortcut icon" type="image/x-icon" href="/images/favicon.ico"/>
    <style type="text/css" media="screen">
        body {
          width: 500px;
          margin-left: auto;
          margin-right: auto;
          font-family: "Trebuchet MS", Verdana, sans-serif;
          background-color: #000;
          color: white;
        }
        #resume {
          text-align : justify;
          font-size: 14px;
          font-style: italic;
        }
        toto {
          position:relative;
        }
    </style>
<?php
include_once("../prgm/functions.php");
include_once("../prgm/langues.php");

preg_match("/FOI_(\d\d)_(\d\d)/",$code,$reg);   # retrouve le mois et l'année dans le code
$an = $reg[1];
$mois = $reg[2];
$test_lang=$langues[$lang];
if ($test_lang!="" and $mois>0 and $mois<13 and $an>01) {
    $arg_ok = 1;   # arguments ok
    $nom_m=$mois_nom[$mois+0];  # +0 pour forcer le passage en nombres
}
# verif qu'il existe :
if ($arg_ok){
    $resum = resume($code,$lang);
    if ($resum == "") {     # happens if lang do not exists
        $resum = resume($code,$deflang);
        if ($deflang=="EN") {
            $ll = $languages[$lang];
            $resum = "Sorry - no summary in $ll\n".$resum;
        } else {
            $ll = $langues[$lang];
            $resum = "Navré - pas de résumé en $ll\n".$resum;
        }        
    }
    $resum = "<p>" . str_replace("\n","</p><p>",$resum) . "</p>\n";
    
} else {
    $resum = "<p></p>";
}
if ($deflang=="EN") {
    echo "<title>Movie Summary</title>";
    $button = "Close this window";
} else {
    echo "<title>Résumé du Film</title>";    
    $button = "Fermer cette fenêtre";
}

?>
	
</head>
<body>
<div id="resume">
<?php
echo $resum;
?>
<input type="button" value=" <?php echo $button ?> " onclick="javascript:window.close();"/>
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
</body></html>
