<?php
 include_once("minitete.php");
 include_once("configuration.php");
 include_once("langues.php");
 
?>

<H1>Liste des langues disponibles</H1>

<table border="1" cellspacing="1" cellpadding="7" style="text-align:center">
<tr>
<th>code</th>
<th>en français</th>
<th>en anglais</th>
<th>dans la langue</th>
<th>le mot résumé</th>
</tr>
<?php
foreach ($ordrelangues as $l) {
  $res = "-";
  @$res = $resume[$l];
  echo "<tr><td>$l</td><td>$langues[$l]</td><td>$languages[$l]</td><td>$lang_self[$l]</td><td>$res</td></tr>";
}
?>
</table>
<form>
<input type=button value="Fermer cette fenêtre" onClick="javascript:window.close();">
</form> 

</body>
</html>
