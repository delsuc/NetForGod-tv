<?php
 include("minitete.php");
 include("functions.php");

@ini_set("zlib.output_compression","0"); // pour permettre l'affichage au fur et a mesure
 
?>

<H1>Mise à Jour du serveur</H1>

<p>C'est parti...</p>
<pre>
Au travail....
<?php
@ob_flush();  flush();
    sleep(1);
    makelog("make_all");
    system($calcul_makeall . " 2>&1");
@ob_flush();  flush();

?>

</pre>
<p>...C'est fait !</p>

<form>
<input type=button value="Fermer cette fenêtre" onClick="javascript:window.close();">
</form> 

</body>
</html>
