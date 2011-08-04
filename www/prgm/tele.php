<?php
 include_once("tete.php");
 include_once("functions.php");
 include_once("bouttons.php");
 include_once("codec.php");
 @$action = $_GET["action"];
 @$page = $_GET["page"];
 @$film =  $_GET["film"];
 @$lang =  $_GET["lang"];
 @$date =  $_GET["date"];
 if ($date == ''){ $date = 7; }
 ?>
	
	<H1>URL de téléchargement temporaires</H1>
	<hr/>
	<h2>Cette page fabrique un lien temporaire permettant le téléchargement d'un film.</h2>
	<p>Cette opération ne crée aucun fichier et ne laisse aucune trace sur le site, vous pouvez donc en faire autant que vous le désirez</p>
	<p>Le code ainsi créé sera ensuite utilisé par la page de téléchargement qui utilise ce code pour déterminer le film à télécharger</p>
	<hr/>
	<h2>Fabrication du lien</h2>
	<form action="tele.php" method="get" accept-charset="utf-8">
	<p>Pour faire le lien il faut spécifier :
	    <ul><li>le film<br/>
			Choisissez la video dans la liste suivante: 
			<select name="film">
		<?php
			foreach (list_FOI() as $file) {
				$titre=titre($file);
				if ($file == $film) {
				  echo "<option value=\"$file\" selected >$file : $titre</option>\n";
				} else {
				  echo "<option value=\"$file\">$file : $titre</option>\n";
				}
			}
		?>
			</select></li>
		<li>la langue du film<br/>
			Choisissez la langue de distribution: 
			<select name="lang">
		<?php
			foreach ($langues as $l => $ll) {
				if ($l == $lang) {
				  echo "<option value=\"$l\" selected >$ll</option>\n";
				} else {
				  echo "<option value=\"$l\">$ll</option>\n";
				}
			}
		?>
			</select><br/>
			ATTENTION, toutes les langues ne sont pas disponibles pour tous les films.</li>
            <li>la durée de validité du lien<br/>
        	            Une fois cette date passée, le lien ne permettra plus le téléchargement.
        	            <br/>
            		    Nombre de jours de validité à partir d'aujourd'hui : 
            		    <input type="text" name="date" value="<?php echo $date ?>" id="date"/>  </li>
        </ul>
    </p>

		<?php
		if ($action) {
		    $todo = "recalculer téléchargement unique";
		    $vid = "$VIDEOdir/$film/$lang"."_divx.avi";
            if (($lang != 'MUL') and (! file_exists($vid))) {
                $tt = $langues[$lang];
                echo "<p><b><big>le film $film n'est pas disponible en $tt!</big></b></p>";
            } else {    
                echo "<hr/>\n<h2>Lien calculé</h2>\n";
                $limit = time() + 3600*24*$date;    # passe en secondes
                $video = substr($film,-2) + 100*substr($film,-5,3);
                $code = codage($limit,$video,$lang);
		echo "<p>A transmettre à l'utilisateur :</p>";
                echo "<p><big> http://$WEBSITE/s/dl.php?c=$code </big></p>";
                echo "<p><big> Le <a href=\"http://$WEBSITE/s/dl.php?c=$code&d=1\" target=\"_blank\">TESTER</a> en rajoutant &amp;d=1 à la fin</big></p><hr/>";
            }
        } else {
             $todo="téléchargement unique";
        }
        ?>
		<input type="submit" name="action" value="<?php echo $todo ?>" id="calculer">
		<?php
		if ($page) {
		    $todo_mul = "recalculer page de téléchargement";
		    $vid = "../FOI/$film/$lang"."_divx.avi";
            echo "<hr/>\n<h2>Lien calculé</h2>\n";
            $limit = time() + 3600*24*$date;    # passe en secondes
            $video = substr($film,-2) + 100*substr($film,-5,3);
            $code = codage($limit,$video,'MUL');
		    echo "<p>A transmettre à l'utilisateur :</p>";
                echo "<p><big> <a href=\"http://$WEBSITE/s/dll.php?c=$code\" target=\"_blank\">http://$WEBSITE/s/dll.php?c=$code </a> </big></p>";
                echo "<p><big> Le <a href=\"http://$WEBSITE/s/dll.php?c=$code&d=1\" target=\"_blank\">TESTER</a> en rajoutant &amp;d=1 à la fin</big></p><hr/>";
        } else {
             $todo_mul = "page de téléchargement";
        }
        ?>
 		<input type="submit" name="page" value="<?php echo $todo_mul ?>" id="calculer">
	</div>
</body>
</html>
