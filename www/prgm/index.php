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
	<H2>Vidéos disponibles:</H2>
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
			foreach (list_video() as $file) {
				$titre=titre($file);
				$titre_en = titre_en($file);
				$cl = click_blank($file);
				echo "<tr><td class=\"ex\">$cl</td><td>$titre<br/><i>$titre_en</i></td>";    # nom de la video
				$cn = count(list_divx($file));
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
				} else {
					echo "<td  class=\"ex\">visible</td>";
				}
				echo "</tr>";
			}
			?>
			</table>
			<p></P>

<hr/>
	<h2>Reste à faire</h2>
	<tr><td><B>Gestion du canal live</B></td>
		<td>	<hr>
		</td>
	</tr>
LIVE
		<td>
			<P>Bascule instantanée sur un canal Live définit</p>
		</td>
	</tr>
ACTUEL
		<td>
			<P>définition du programme actuel</p>
		</td>
	</tr>
</table>
</div>
</body>
</html>
