<?php
 include_once("tete.php");
 include_once("functions.php");
 include_once("actions.php");
 include_once("bouttons.php");
 ?>

<H1>Diagnostic du serveur</H1>
<p>Cette page permet de détecter les problèmes au moment du calcul, et d'en suivre l'avancement </p>

<hr width="30%">
<h2>journal du traitement sur le serveur</H2>
    <a href="make.log" target="_blank" >make.log</a>

<hr width="30%">
<h2>journal du traitement sur la machine de postproduction</H2>
    <a href="post-prod/make.log" target="_blank" >post-prod - make.log</a>

<hr width="30%">
<h2>diagnostic PHP code set-up</H2>
    <a href="debug.php" target="_blank" >debug code</a>

<hr width="30%">
<h2>diagnostic PHP installation</H2>
    <a href="php.php" target="_blank" >PHPInfo()</a>

</body>
</html>
