<?php
 include_once("tete.php");
 include_once("functions.php");
 include_once("actions.php");
 include_once("bouttons.php");
 ?>
	
	<H1>Outils divers</H1>
	<hr/>
    <h2>Attention Page en développement, cette partie est Ok</h2>
        <hr/>
        <H2>calcule de téléchargements temporaires:</H2>
        <p>Pour donner (ou vendre) des films en haute Résolution.</p>
    <input type="submit" name="tele" value="Calculer téléchargement"
onclick="javascript:window.location.href='tele.php'">

            <hr/>
    <h2>Etat du pipe-line de production</h2>
    <ul>
    <li>la ligne qui suit indique si un calcul de compression video est actuellement en cours
    <?php
    if (travail_bloque()) {
       $act=""; $nonact='class="ex"';
    } else {
       $act='class="ex"';$nonact='';
    }
    $dur=travail_en_cours();
    if ($dur) {
        $work='<span class="ex" >Travail en cours</span>';   $nonwork='';
    } else {
        $work=""; $nonwork='<span class="ex" >Pas de Travail en cours</span>';
    }

    ?>
    <form action="index.php" method="get" accept-charset="utf-8">
    <p>
    <?php 
    if ($dur) {
        echo '<span class="ex" >Travail en cours</span>';
        echo " depuis $dur secondes";
    } else {
        echo '<span class="ex" >Pas de Travail en cours</span>';
    }
     ?>
    </p>
    </li>
    <li>Le bouton suivant permet de bloquer le pipeline. Cela n'arrète pas un calcul en cours, mais ca empèche que les calculs automatiques soient lancés
    <p>
    PipeLine : <span <?php echo $act; ?> >Activ&eacute;</span> / 
    <span <?php echo $nonact; ?> >Inactiv&eacute;</span> - 
    <input type="submit" name="action" value="Inverser l'état">
    </p>
    </li>
    </ul>
    </form>

	<hr/>
	<H2>Langues disponibles:</H2>
        <p>Les langues affichées ici sont les langues gérées par le programme.
          si une langue manque, il faut contacter 'administrateur de ce site.</p>
    <input type="submit" name="langues" value="Afficher les langues disponibles" onclick="openWindow('calc_lang.php','calc_lang');">

	<hr/>
	<H2>Place sur le disque</H2>
	<?php
    $szt = round(10*disk_total_space($VIDEOdir) / 1024/1024/1024);
	$szr = round(10*disk_free_space($VIDEOdir) / 1024/1024/1024);
	$szbib = `du -sh $VIDEOdir`;
	?>
	<p>Taille totale du disque dur : <?php echo $szt/10 ?> Go </p>
	<p>Place restante sur le disque : <?php echo $szr/10 ?> Go </p>
	<p>Taille de la bibliothèque de films : <?php echo $szbib ?></p>
	<input type="submit" name="Places" value="Afficher la tailles des films" onclick="openWindow('calc_size.php','calc_size');">
	<hr/>
    <H2>reste à faire :</H2>
    <li> changer les titres
    <li> changer les affiches
    <li> changer les photos
    <li> effacer un film

</div>
</body>
</html>
<!-- <H2>Cette partie n'est pas finie, NE PAS ENCORE UTILISER</H2>

<h2>Modifier les éléments</h2>
     <p>Ces boutons permettent de modifier les éléments du site sans passer par la machine de post-production<br/>
         </p>
         <table border="1" cellspacing="5" cellpadding="5" style="text-align:center">
             <tr>
                 <th><i>Pages</i></th>
                 <th><i>titre</i></th>
                 <th><br><i>Action</i></th>
             </tr>
             <tr><td><a href="/VOD" target="blank">Page VOD</a></td><td>NetForGod TV</td>
                 <td>
                   <input type="submit" name="action" value="Recalculer" onclick="openWindow('calc_vod.php','calc_vod');">
                 </td>
             </tr>
         <?php
         // foreach (list_video() as $file) {
         //         $titre=titre($file);
         //         $titre_en = titre_en($file);
         //         $cl = click_blank($file);
         //         echo "<tr><FORM action=\"calc_tele.php\" method=\"get\"><input type=\"hidden\" name=\"video\" value=\"$file\"/>\n";
         //         echo "<td>$cl</td>";
         //         echo "<td><textarea name=\"titre_FR\" rows=\"2\" cols=\"40\">$titre</textarea>\n";
         //         echo "<textarea name=\"titre_EN\" rows=\"2\" cols=\"40\">$titre_en</textarea></td>\n";
         //         echo "<td><input type=\"submit\" name=\"action\" value=\"Recalculer\" ></td></tr>\n";
         //     }
         ?>
         </table>
         <p></P>

        <hr/>
 -->
