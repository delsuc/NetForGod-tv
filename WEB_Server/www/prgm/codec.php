<?php 
// Outils pour le codage et decodage des url pour le téléchargement payant des films
// Ce fichier ne sera execute qu'une fois

include_once("langues.php");
date_default_timezone_set("Europe/Paris");

$prim1 = 3511;
$prim2 = 67;
$prim3 = 13;
$crclen = 5;

$debug = 0;     # mettre à 0 pour production 

function codage($date_sec,$video,$lang)    {
    # return une chaine qui "crypte" (très faiblement) les champs
    # i) date_sec est transformée en jours depuis le 1 1 2009
    # ii) lang est transformée dans l'index dans la table globale
    # iii) date lang et video sont mélangés avec des nmbre premiers prim1 et prim2
    # iv) le nombre est codé en base 35
    # v) les derniers chiffres du crc codé en base 33 sont rajoutés à la fin
    global $ordrelangues, $prim1,$prim2,$prim3,$crclen;
    global $debug;
    
    #trouve index de langue
    $count = 0;
    $ilang = 0;
    foreach ($ordrelangues as $ien) {
        $count++;
        if ($ien == $lang) { $ilang = $count; }
    }
    $date = floor($date_sec/3600) - 39*24*365;  # change la date en heures depuis le ~ 1 1 2009
    $descrip = ($date*$prim1 + $video)*$prim2 + $ilang; # je préfère que la langue soit facile à piratée
    $crc = base_convert(crc32($descrip),10,35); # rajoute un crc
    $descrip = $descrip * $prim3;       # puis multiplie par prim3
    $crc = substr($crc,-$crclen); # garde les 5
    $value = base_convert($descrip,10,33);  # en base 33
    if ($debug == 1) {
        echo "ilang : $ilang<br/>";
        echo "video : $video<br/>";
        echo "date : $date<br/>";
        echo "descrip : $descrip<br/>";
        echo "crc : $crc<br/>";
        echo "value : $value<br/>";
        echo "return : $value$crc<br/>";
    }
    return "$value$crc";
}
function decodage($val1)  {
    # inverse codage
    global $ordrelangues, $prim1,$prim2,$prim3,$crclen;
    global $debug;
    
    $crc = substr($val1,-$crclen);
    $v = substr($val1,0,-$crclen);
    $val = base_convert($v,33,10);  # en base 33
    $val = floor($val / $prim3);

    $check = base_convert(crc32($val),10,35); # rajoute un crc
    #trouve index de langue
#    $descrip = ($date*$prim1 + $video)*$prim2 + $ilang;   
    $dd = floor($val/$prim2);
    $il = floor($val - $dd*$prim2); # ATTENTION % est buggé sur PHP -en tout cas ici - !!!!! Hallucinant !!!
    $lang = $ordrelangues[$il-1];
    $video = floor($dd % $prim1);
    $date = floor($dd / $prim1) + 39*24*365;
    if ($debug == 1) {
        echo "crc : $crc<br/>";
        echo "value : $val<br/>";
        echo "video : $video<br/>";
        echo "lang : $il $lang<br/>";
        echo "date : $date<br/>";
    }
    if ($crc !=  substr($check,-$crclen)) {  # CRC error
        $date=0;
        $video=0;
        $lang=0;
    }
    return array($date,$video,$lang);
}

function test_code($jours,$video,$lang) {
        global $debug;
        $date = time() + 3600*24*$jours;  #date de validite  time() donne le nbre de secondes depuis le 1 1 1970, à aujourd'hui
        echo "date : $jours $date<br/>";
        echo "video : $video<br/>";
        echo "lang : $lang<br/>";
        echo "========codage<br/>";
        $code = codage($date,$video,$lang);
        echo "========decodage<br/>";
        $t = decodage($code);
        if ($debug == 0 ) {
                $d = $t[0];
                $v = $t[1];
                $l = $t[2];
                printf("decoded film : FOI_%s_%04d<br/>",$l,$v);
                printf("decoded validite : %06d  : ",$d);
                $valid = getdate($d*3600);
                echo "$valid[mday] $valid[mon] $valid[year]<br/>";
        }
        return $t;
}

function test_test() {
    $jours = 30;
    $video = "0712";    #date du film  YY-MM  ==>  max = 2000 si 2020
    $lang = "MUL";
    echo "<br/>";
    $t = test_code($jours,$video,$lang);
    echo "<hr/>";
    $t = test_code($jours+1,$video,$lang);
    echo "<br/>";
}
if ($debug == 1) {test_test();}
?>
