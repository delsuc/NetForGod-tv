<?php
 include_once("minitete.php");
 include_once("configuration.php");

@ini_set("zlib.output_compression","0"); // pour permettre l'affichage au fur et a mesure
 
?>

<H1>Liste des langues disponibles</H1>

<pre>
<?php
@ob_flush();  flush();
    sleep(1);
    system("cd $MAKEdir; python langues.py");
@ob_flush();  flush();

?>

</pre>

<form>
<input type=button value="Fermer cette fenêtre" onClick="javascript:window.close();">
</form> 

</body>
</html>
