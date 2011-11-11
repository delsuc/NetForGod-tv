<?php
include_once("tete.php");
include_once("bouttons.php");
include_once("functions.php");
$szbib = `du -sh $VIDEOdir | awk '{print $1}'`;
?>
	
<H1>Statistiques sur le contenu</H1>
<hr width="30%">
<ul>
    <li>Le site comporte
    <ul>
        <li> <?php echo count(list_video());?> films multilangues (HD et streaming)</li>
        <li> qui prennent <?php echo $szbib;?> sur le disque dur</li>
        <li>qui représenteent en tout <?php 
        $cc = 0;
        foreach (list_video() as $i) { $cc += count(list_divx($i)); }
        echo $cc;
        ?> videos indépendantes qui sont distribuées</li>
    </ul>
    <li>Il y a  <?php 
    $cc = 0;
    foreach (list_video() as $i) {
        if (est_public($i)) { $cc += 1; }
    }
    echo $cc;
    ?> films publiques</li>
    <li>Il y a <?php echo (count(list_video())-$cc);?> films privés</li>
</ul>
<hr width="30%">
<H1>Statistiques sur les visites</H1>
<hr width="30%">
<h3> Statististiques générales du site
</h3>
<ul>
<li><a href="https://www.google.com/analytics/settings/?et=reset&hl=fr-FR">Google Analytics</a> - statistique très fouillées sur les pages publiques, mais nécesite un compte chez Google.</li>
</ul>
<hr width="30%">
<h3>Statistique de la partie VOD (<i>pas encore fonctionnel</i>)</h3>
<ul>
<li>de <a href="http://<?php echo $WEBSITE; ?>/FOI_stats/VOD_stats.html" title="statistiques de VOD"> Visites </a> des vidéos en VOD.
</li>
</ul>
<hr width="30%">
<h3>Statistique de la partie téléchargement</h3>
    <p><a href="http://<?php echo $WEBSITE; ?>/stat_nfg.html">Récapitulatif</a> de tous les film.</p>

	<table border="1" cellspacing="5" cellpadding="5" style="text-align:center">
		<tr><th><i>Vidéo</i></th>
			<th><i>titre</i></th></tr>
    		<?php
    		foreach (rlist_video() as $file) {
    			$titre=titre($file);
    			$cl = click($file);
    			echo "<tr><td><a href=\"$urldivx/$file/stat.html\">$file</a></td>";
    			echo "<td>$titre</td>";    # nom de la video
    			echo "</tr>";
    		}
    		?>

</table>



<hr width="30%">

</div>
</body>
</html>
