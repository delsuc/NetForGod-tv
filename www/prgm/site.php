<?php
 include_once("tete.php");
 include_once("functions.php");
 include_once("actions.php");
 include_once("bouttons.php");

 ?>

<H1>Gestion des accès aux différentes pages du site</H1>
<hr/>
<h2>Contenu de la page VOD</H2>
	<p>Par cette page on peut gérer quelles vidéo sont disponibles sur la page de la <a href="<?echo $urlvod?>">VOD</A></P>
	<p>Pour chaque vidéo on peu choisir si elle est visible ou non sur la page de VOD<br/>
	Celà est indépendant du fait que la vidéo soit téléchargeable ou pas.</p>
	<p>Pour changer l'état, il faut cocher les cases voulues et cliquer sur le bouton "Changer les droits".</p>
	<p>Par contre la page de VOD n'est pas recalculée, pour cela il faut aller à la page <a href="content.php">Contenu</a></p>
	<form action="site.php" method="get" accept-charset="utf-8">
		<table border="1" cellspacing="5" cellpadding="5" style="text-align:center">
			<tr><th><i>Vidéo</i></th>
				<th><i>titre</i></th>
				<th><i>visible sur<br/>la page VOD</i></th>
				<th><i>en tête sur <br/>la page VOD</i></th></tr>
		<?php
		foreach (rlist_video() as $file) {
			$titre=titre($file);
			$cl = click($file);
			echo "<tr><td class=\"ex\">$cl</td><td>$titre</td>";    # nom de la video
			echo "<td><input type=\"checkbox\" name=\"$file\"";
			if (! est_cachee($file)) { echo " checked "; }
			echo "/></td>";
			echo "<td><input type=\"radio\" name=\"premier\" value=\"$file\"";
			if (est_premier($file)) { echo " checked "; }
			echo "/></td>";
			echo "</tr>";
		}
		?>
		<tr><td colspan="3"><input type="submit" name="action" value="Changer les droits"></td></tr>
	</table>
	</form>

<hr/>
		
</body>
</html>
