<?php  $uri = $_SERVER["REQUEST_URI"];  ?>
<div id="bouttons">
<ul>
<li>    <?php
    $pos = strpos($uri, "doc.php");
    if ($pos === false) {       # YES ! === !
    	echo '<a href="doc.php" title="Documentation">Doc</a>';
    } else {
    	echo 'Doc';
    }
    ?>
</li>
<li>  <?php
    $pos = strpos($uri, "index.php");
    if ($pos === false) {       # YES ! === !
    	echo '<a href="index.php" title="Retour à la page d\'accueil">Accueil</a>';
    } else {
    	echo 'Accueil';
    }
    ?>	
</li>
<li>	<?php
    $pos = strpos($uri, "site.php");
    if ($pos === false) {       # YES ! === !
    	echo '<a href="site.php" title="gestion de l\'accès au site">Accès</a>';
    } else {
    	echo 'Accès';
    }
    ?>
</li>
<li>	<?php
    $pos = strpos($uri, "content.php");
    if ($pos === false) {       # YES ! === !
    	echo '<a href="content.php" title="Gérer le contenu">Contenu</a>';
    } else {
    	echo 'Contenu';
    }
    ?>
</li>
<li>	<?php
    $pos = strpos($uri, "utils.php");
    if ($pos === false) {       # YES ! === !
    	echo '<a href="utils.php" title="Outils divers">Outils</a>';
    } else {
    	echo 'Outils';
    }
    ?>
</li>
<li>	<?php
    $pos = strpos($uri, "stats.php");
    if ($pos === false) {       # YES ! === !
    	echo '<a href="stats.php" title="Visualiser des statistiques de téléchargement">Statistiques</a>';
    } else {
    	echo 'Statistiques';
    }
    ?>
</li>
<li> <?php
    $pos = strpos($uri, "diag.php");
    if ($pos === false) {       # YES ! === !
    	echo '<a href="diag.php" title="Diagnostic de problèmes éventuels">Diagnostic</a>';
    } else {
    	echo 'Diagnostic';
    }
    ?>
</li>
</ul>
<br/>
</div>
