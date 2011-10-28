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
        <li> <?php echo count($list_video);?> films multilangues (HD et streaming)</li>
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
    <li>Il y a <?php echo (count($list_video)-$cc);?> films privés</li>
</ul>
<hr width="30%">
<H1>Statistiques sur les visites (<i>pas encore fonctionnel</i>)</H1>
<hr width="30%">
<h3>Statistique de la partie VOD et téléchargement</h3>
<ul>
<li>de <a href="http://www.netforgod.tv/FOI_stats/download_stats.html" title="statistiques de téléchargement">
	Téléchargement
</a> de la vidéo du mois en haute qualité.
</li>
<li>de <a href="http://www.netforgod.tv/FOI_stats/VOD_stats.html" title="statistiques de VOD"> Visites </a> des vidéos en VOD.
</li>
</ul>
<hr width="30%">
<h3> Statististiques générales du site
</h3>
<ul>
<li><a href="http://www.netforgod.tv/munin-monitoring/netforgod.tv/www.netforgod.tv.html">munin</a>
- courbes d'état du serveur en temps réel</li>
<li><a href="http://www.netforgod.tv/webalizer">Webalizer</a> - statistiques mensuelles simplifiées </li>
<li><a href="http://www.netforgod.tv/awstats/awstats.pl">awstats</a> - statistiques mensuelles détaillées</li>
<li><a href="https://www.google.com/analytics/settings/?et=reset&hl=fr-FR">Google Analytics</a> - statistique très fouillées sur les pages publiques, mais nécesite un compte chez Google.</li>
</ul>
<hr width="30%">

</div>
</body>
</html>
