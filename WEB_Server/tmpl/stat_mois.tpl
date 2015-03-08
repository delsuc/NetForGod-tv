<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en,fr" xml:lang="en,fr" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<meta content="Statistics page " name="description" />
<title> Statistiques des t&eacute;l&eacute;chargement des films {{baseurl}} pour  {{basename}}</title>
<style type="text/css">
body {font-size:12pt; font-family: verdana,sans-serif; color=#FFFFCC;}
.centre {margin-left:auto; margin-right:auto; text-align:center;}
table {text-align:left;}
</style>
</head>
<body bgcolor="#000000" text="#FFFFCC"  link="#FF0033">
<centre>
<H1>Statistiques de t&eacute;l&eacute;chargement des films {{baseurl}}</H1>
<p><i>d&eacute;termin&eacute;es le {{now}}</i></p>
<h2>{{basename}} <br/> {{Total}} t&eacute;l&eacute;chargements uniques</h2>
<p><i>Pour {{Tototal}} t&eacute;l&eacute;chargements en tout</i></p>
</centre>
<HR>
<table border="0" cellspacing="1" cellpadding="1">
    <tr><th>Langues</th><th>nombre</th><th COLSPAN="2">% du Total du mois</th><th> <i>Erreurs</i></th>
    </tr>
    %for i in sorted(stat_t.keys(), key = lambda s:stat_n[s], reverse=True):
    <tr>
        <td>{{ll[i]}}</td> <td>{{stat_n[i]}}</td>
        <td>{{(100*stat_n[i])/Total}}%</td>
        <td> <img src="http://{{baseurl}}/images/hp.png" width="{{(200*stat_n[i])/Total}}" height="10"></td>
        <td>
        %if stat_n[i] != len(stat_t[i]):
             (<i>+ {{len(stat_t[i])-stat_n[i]}} multi-t&eacute;l&eacute;chargements</i>)
        %end
        </td>
    </tr>
    %end
</table>
<HR>
        <p><b>t&eacute;l&eacute;chargements par jour</b></p>
        <table>
        <tr valign="bottom">
        %vratio = 2
        %for i in sorted(stat_d):
            %dl = len(stat_d[i])
            <td><img align="bottom" src="http://{{baseurl}}/images/vp.png" height="{{dl}}" width="8" alt='Nombre de visites: {{dl}}' title='Nombre de visites: {{dl}}' /></td>
        %end
        </tr>
        <tr valign="middle">
        %for i in sorted(stat_d):
            <td><span alt='date: {{i}}' title='date: {{i}}'>{{i[-2:]}}</span></td>
        %end
        </tr>
    </table>

    <p><b>t&eacute;l&eacute;chargements cumul&eacute;s depuis le lancement.</b></p>
    <table>
    <tr valign="bottom">
    %totdl = 0
    %for i in sorted(stat_d):
        %totdl += len(stat_d[i])
        <td><img align="bottom" src="http://{{baseurl}}/images/vh.png" height="{{totdl/vratio}}" width="8" alt='Nombre total de visites: {{totdl}}' title='Nombre total de visites: {{totdl}}' /></td>
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
</body>
</html>
