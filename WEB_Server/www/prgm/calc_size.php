<?php
 include_once("minitete.php");
 include_once("functions.php");

@ini_set("zlib.output_compression","0"); // pour permettre l'affichage au fur et a mesure
 
?>

<H1>Liste des films disponibles</H1>

<pre>
<?php
foreach (list_video() as $file) {
    $sz = `du -sh $basevideos/$file/`;
    echo "$sz <br/>";
}
?>

</pre>

<form>
<input type=button value="Fermer cette fenêtre" onClick="javascript:window.close();">
</form> 

</body>
</html>
