<?php
 include_once("tete.php");
 include_once("functions.php");
 include_once("actions.php");
 include_once("bouttons.php");
 ?>

        <H1>Gestion du contenu</H1>
<p>Cette page permet de modifier le contenu du site</p>

        <hr/>
<h2>Mettre à jour toutes les pages du serveur</H2>
    <p>Ce bouton force le lancement du calcul qui est fait automatiquement toutes les heures (<i>calcul des nouveaux DivX, calcul des nouveaux flash, actualisation des pages Web </i>)<br/>
        Utile, quand on pressé de valider un nouveau téléchargement.</p>
    <p><b>Ne pas en abuser !</b></p>
<?php if (! travail_en_cours()) { ?>
	<input type="submit" name="action" value="Mettre A Jour" onclick="openWindow('calc_makeall.php','calc_makeall');">
<?php } else { ?>
	<i> - action d&eacute;sactiv&eacute;e car le pipe-line est d&eacute;j&agrave; en train de travailler - </i>
<?php } ?>

             <hr/>
<h2>Forcer la mise à jour des différentes pages visibles</h2>
    <p>Ces boutons forcent la mise à jour des pages du serveur WEB, même si il n'y a pas d'éléments nouveaux<br/>
        Utile, en cas de problèmes ou cas particuliers uniquement, ou quand un élément a été modifiés manuellement.</p>
    <p><b>Utiliser à bon escient !</b></p>
    
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
    foreach (list_video() as $file) {
            $titre=titre($file);
            $titre_en = titre_en($file);
            $cl = click_blank($file);
            echo "<tr><td>$cl</td><td>$titre<br/><i>$titre_en</i></td>\n";    # nom de la video

           echo "<td><input type=\"submit\" name=\"action\" value=\"Recalculer\" onclick=\"openWindow('calc_tele.php?video=$file','calc_tele');\">";
            echo" </td>\n";
            echo "</tr\n>";
    }
    ?>
    </table>
    <p></P>


         <hr/>

</div>
</body>
</html>
