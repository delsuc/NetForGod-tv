<?php
include_once("tete.php");
include_once("configuration.php");
include_once("functions.php");
?>
<H1> List of configuration parameters </H1>
<h2>Global variables</h2>
<ul>
    <li> URL :<?php  echo "$WEBSITE";?></li>
    <li> COPYRIGHT : <?php echo $COPYRIGHT; ?></li>
    <li> WEBROOT : <?php echo $WEBROOT; ?></li>
    <li> MAKEdir : <?php echo $MAKEdir; ?></li>
    <li> VIDEOdir : <?php echo $VIDEOdir; ?></li>
    <li> VODdir : <?php echo $VODdir; ?></li>
</ul>
<h2>Global computed Lists</h2>
<ul>
    <li> list_video <?php print_r($list_video); ?> </li>
    <li> list_FOI <?php print_r($list_FOI); ?> </li>
</ul>
</body>
</html>    

