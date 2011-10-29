<?php
 include_once("tete.php");
 include_once("functions.php");
 include_once("actions.php");
 include_once("bouttons.php");
 ?>
	
	<H1>Page D'administration</H1>
	<hr/>
    <h2>Attention </h2>
	<p><i>Ce projet est encore de développement, tout n'est pas actif'</i></p>

	<hr/>
	<H2>Vidéos disponibles: <I><?php echo count(list_video()) ?> films multilangues en tout</I></H2>
			<table border="1" cellspacing="5" cellpadding="5" style="text-align:center">
				<tr><th><i>Vidéo<br>disponibles</i></th>
				<th><i>titre</i></th>
				<th><i>nb de<br/>langues</i></th>
				<th><i>au<br>tele.</i></th>
				<th><br><i>état sur la<br/>page VOD</i></th></tr>
                                <tr>
                                <td><a href="/VOD" target="blank">VOD</a></td>
                                <td>NetForGod TV</td>
<td>2</td><td>-</td><td>-</td>
                                </tr>
			<?php
			$cache = 0;
			$visi = 0;
			$divx = 0;
			foreach (list_video() as $file) {
				$titre=titre($file);
				$titre_en = titre_en($file);
				$cl = click_blank($file);
				echo "<tr><td class=\"ex\">$cl</td><td>$titre<br/><i>$titre_en</i></td>";    # nom de la video
				$cn = count(list_divx($file));
				$divx += $cn;
				echo "<td>$cn</td>";
//                                $sz=`du -sh $basevideos/$file/`;
 //                               echo "<td>$sz</td>";
				if ($file == video_du_mois()) {
					echo "<td  class=\"ex\">X</td>";		# la video du mois
				} else{
					echo "<td></td>";
				}
				if (est_cachee($file)) {
					echo "<td>cachée</td>";		# la video est cachée
					$cache += 1;
				} else {
					echo "<td  class=\"ex\">visible</td>";
					$visi += 1;
				}
				echo "</tr>";
			}
			?>
			</table>
<p>Ce qui fait <?php
echo "$visi films visibles et $cache films cachés pour un total de $divx vidéos différentes.";
?> </p>

<hr/>
</body>
</html>
