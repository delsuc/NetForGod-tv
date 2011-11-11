<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en,fr" xml:lang="en,fr" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<meta content="Statistics page " name="description" />
<title>Statistiques des t&eacute;l&eacute;chargement des films {{baseurl}}</title>
<style type="text/css">
body {font-size:12pt; font-family: verdana,sans-serif; color=#FFFFCC;}
.centre {margin-left:auto; margin-right:auto; text-align:center;}
table {text-align:left;}
</style>
</head>
<body bgcolor="#000000" text="#FFFFCC"  link="#FF0033">
<centre>
<H1>Statistiques de t&eacute;l&eacute;chargement des films {{baseurl}}</H1>
<p>Ces statistiques comptent &agrave; partir de la cr&eacute;ation du site</p>
<h2>{{TTotal}} t&eacute;l&eacute;chargements</h2>
</centre>
<HR>
    <h2>Statistiques par film</h2>
<table border="0" cellspacing="1" cellpadding="1">
    <tr><th>Film</th><th COLSPAN="2">nombre de t&eacute;l&eacute;chargements uniques (<i>total</i>)</th><th></th>
    </tr>
    %for i in sorted(stat_film.keys(), reverse=True):
    <tr>
        <td><a href="videos/{{i}}/stat.html" >{{i}}</a>&nbsp;</td> <td>&nbsp;{{stat_film[i]}} (<i>{{stat_tfilm[i]}}</i>)</td>
        <td> <img src="http://{{baseurl}}/images/hp.png" width="{{stat_film[i]}}" height="10"></td>
    </tr>
    %end
</table>
<HR>
    <h2>Statistiques par langue</h2>
<table border="0" cellspacing="1" cellpadding="1">
    <tr><th>Langues</th><th>nombre</th><th COLSPAN="2">% du Total</th>
    </tr>
    %for i in sorted(stat_lang.keys(), key = lambda s:stat_lang[s], reverse=True):
    <tr>
        <td>{{ll[i]}}</td> <td>{{stat_lang[i]}}</td>
        <td>{{(100*stat_lang[i])/TTotal}}%</td>
        <td> <img src="http://{{baseurl}}/images/hp.png" width="{{(200*stat_lang[i])/TTotal}}" height="10"></td>
    </tr>
    %end
</table>
<HR>
<h2>Statistiques par jour</h2>
    <table>
    <tr valign="bottom">
    %for i in sorted(stat_d):
        <td><img align="bottom" src="http://{{baseurl}}/images/vp.png" height="{{int(1.0*stat_d[i])}}" width="8" alt='Nombre de visites: {{stat_d[i]}}' title='Nombre de visites: {{stat_d[i]}}' /></td>
    %end
    </tr>
    <tr valign="middle">
    %for i in sorted(stat_d):
        <td><span alt='date: {{i}}' title='date: {{i}}'>{{i[-2:]}}</span></td>
    %end
    </tr>
</table>
<p><i>mettre la souris sur la barre pour avoir le nombre exact, et sur le chiffre pour avoir la date exacte</i></p>
<HR>
<h2>Grands telechargeurs</h2>
    <table>
    <tr valign="bottom">
    %for i in sorted(stat_ip.keys(), key = lambda s:stat_ip[s], reverse=True):
        %if stat_ip[i]<20: break
        <td><img align="bottom" src="http://{{baseurl}}/images/vp.png" height="{{int(1.0*stat_ip[i])}}" width="8" alt='{{stat_ip[i]}} downloads' title='{{ipnm[i]}} {{stat_ip[i]}} downloads' /></td>
    %end
    </tr>
</table>
</body>
</html>
