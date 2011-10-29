# -*- coding: utf-8 -*-
"""
library for the FOI project 

Le différentes classes permettent de fabriquer pour chaque film les pages spécifiques :
diaporama : pour les visuels du film
presentation : affiche, liens vers les résumés et diaporama
index : page de base avec video, et lien vers les autres pages
"""

import langues
import os, sys
import glob
import re
import os.path as op


footer="""
<BR CLEAR=ALL>
<div id="pied">
<ul>
<li><a href="/media/copyright.html">&copy; C.C.N.</a></li>
<li>| <a href="http://chemin-neuf.org">La communaut&eacute; du Chemin-Neuf </a> | </li>
<li><a href="/media/mentions.html">mentions l&eacute;gales</a> | </li>
<li><a href="mailto:netforgod@chemin-neuf.org?cc=nfg.webmaster@gmail.com&amp;subject=depuis le site netforgod.tv" >contactez-nous</a> | </li>
<li>Ce site est optimis&eacute; pour Firefox</li>
</ul></div></div></div></body></html>
"""

def chop_nl(list_of_strings):
    """removes \n at the end of all lines"""
    for i in range(len(list_of_strings)):
        list_of_strings[i] = list_of_strings[i].rstrip("\n")

def clean(st):
    """nettoie les characteres interdit en HTML"""
    return st.replace("&","&amp;").replace("'","&#x27;").replace('"',"&quot;").replace("\n","<br/>").replace("\r","")

def current_title(dir):
    from os.path import join
    """ lit les fichiers titre_EN.txt et titre_FR.txt """
    tis = glob.glob(join(dir,"textes","titre_*.txt"))
    (ti_FR,ti_EN) = (("pas de titre",),("no title",))
    for f in tis:
        if f.endswith('_FR.txt'):
            ti_FR = file(f).readlines()
            chop_nl(ti_FR)
        if f.endswith('_EN.txt'):
            ti_EN = file(f).readlines()
            chop_nl(ti_EN)
    return((ti_FR,ti_EN))

def current_resume(dir):
    """ lit les fichiers resume_EN.txt et resume_FR.txt """
    from os.path import join
    tis = glob.glob(join(dir,"textes","resume_*.txt"))
    (ti_FR,ti_EN) = ("pas de resume","no synopsis")
    for f in tis:
        if f.endswith('_FR.txt'):
#            ti_FR = "<BR>".join(file(f).readlines())
            ti_FR = file(f).readlines()
            chop_nl(ti_FR)
        if f.endswith('_EN.txt'):
            ti_EN = file(f).readlines()
            chop_nl(ti_EN)
    return((ti_FR,ti_EN))

def current_date_2():
    import datetime
    mois = datetime.datetime.today().month
    an = datetime.datetime.today().year
    return(an,mois)

def current_date(dir):
    import time
    ici = op.basename(op.abspath(dir))
    try:
        [(annee,mois)] = re.findall("FOI_(\d\d)_(\d\d)",ici)
        annee = 2000+int(annee)
    except:
        lt = time.localtime()
        annee = lt[0]
        mois = lt[1]
    return(int(annee),int(mois))

def read_dir(dir,template="*"):
    divx = glob.glob(op.join(dir,template))
    return divx



class diaporama:
    """permet de créer des diaporama"""

    def __init__(self, dir,lang="FR"):
        try:
            import Image    # Python Image Library is required - see 
        except:
            raise "Python Image Library is required - see  http://www.pythonware.com/products/pil/ "
        self.dir = dir
        (self.annee,self.mois)=current_date(self.dir)
        self.setLang(lang)
        imlist = glob.glob(op.join(self.dir,"images","photo*.jpg"))
        self.empty = len(imlist)==0 # tells that there is no diaporama to do
        self.texte="""\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" >
<meta content="NetForGod page " name="description" >
<title>%(flat_title)s</title>
<!-- This page uses SimpleViewer 
    Download SimpleViewer at www.airtightinteractive.com/simpleviewer -->
<script type="text/javascript" src="/js/swfobject.js"></script>
<STYLE TYPE="text/css">
a { text-decoration: none;}
.bd-droit {float: right; width: 148px; text-align: center;}
</STYLE>
<script type="text/javascript">
function diapo() {
               var fo = new SWFObject("/s/viewer.swf", "viewer", "100%%", "700", "7", "#181818");
               fo.addVariable("preloaderColor", "0xffffff");
               fo.addVariable("xmlDataPath", "gallery_%(lang)s.xml");
               fo.write("flashcontent");
               var x=document.getElementById("flashcontent").style.height=700;
               }
</script>
</head>
<body onload="diapo()" bgcolor="#000000" text="#FFFFCC"  link="#FF0033" style="font-size:12pt; font-family: verdana,sans-serif; color=#FFFFCC">
<div style="margin-left:auto; margin-right:auto; text-align:center;">
<div class="bd-droit">
%(link)s
</div>
<div style="width:1000px; margin-left:auto; margin-right:auto; text-align:center;">
<p> %(mois)s %(annee)d - <b>%(br_titre)s</b></p>
       <div id="flashcontent">
SimpleViewer requires Macromedia Flash. <a href="http://www.macromedia.com/go/getflashplayer/">Get Macromedia Flash.</a> If you have Flash
installed, <a href="diaporama_%(lang)s.html?detectflash=false">click to view gallery</a>.</div>
</div>
<p style="text-align:center"> FRATERNITÉ ŒCUMÉNIQUE INTERNATIONALE - - NET FOR GOD - - INTERNATIONAL ECUMENICAL FRATERNITY </p>
</div>
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%%3E%%3C/script%%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-4576934-2");
pageTracker._initData();
pageTracker._trackPageview();
</script>
</body>
</html>
"""

    def setLang(self,lang):
        """docstring for setLang"""
        self.lang=lang
        (titre_fr,titre_en)=current_title(self.dir)
        if self.lang=="FR":
            self.slogan="Au service de l'UNITÉ des CHRÉTIENS et de la PAIX dans le MONDE."
            self.discover="Découvir la fraternité NetForGod"
            self.presname="presentation.html"
            self.diaponame="diaporama.html"
            self.resname="resume.html"
            self.resume="Résumé du film"
            self.titre=titre_fr
            self.nomMois=langues.mois_nom[self.mois]
            self.link="""Français<a href="diaporama_EN.html"> / English</a>"""  # attention, non généralisable
        elif self.lang=="EN":
            self.slogan="Working for Christian unity and for peace in the world !"
            self.discover="Discover the NetForGod fraternity"
            self.presname="presentation_EN.html"
            self.diaponame="diaporama_EN.html"
            self.resname="resume_EN.html"
            self.resume="Movie synopsis"
            self.titre=titre_en
            self.nomMois=langues.month_name[self.mois]
            self.link="""English <a href="diaporama.html">/ Français</a>"""

    def images(self,maxsiz=(720,576),thumbsiz=(80,72)):
        """
        goes through all jpg files in self.dir/images/* 
        scale them to maxsiz
        creates thumbnails and save them in self.dir/thumbs/*
        """
        import Image
        if not op.exists(op.join(self.dir,"thumbs")):
            os.mkdir(op.join(self.dir,"thumbs"))
        for ii in glob.glob(op.join(self.dir,"images","photo*.jpg")) :
            im=Image.open(ii)
            if 1.1*max(maxsiz)<max(im.size):    # needs to undersample
                print "je reduis %s  taille : %s"%(ii, str(im.size))
                HQ = op.join(op.dirname(ii),"HQ_"+op.basename(ii))    # images/photo*.jpg => images/HQ_photo*.jpg
                im.save(HQ)  # makes a backup
                im.resize(maxsiz,Image.ANTIALIAS)
                im.save(ii)
            ith=ii.replace("images/","thumbs/")
            if not op.exists(ith):     # makes thumbnail
                im.thumbnail(thumbsiz,Image.ANTIALIAS)
                im.save(ith)

    def do_xml(self):
        """
        takes photos in images/photoxx.jpg and captions in textes/photoxx_LL.jpg
        and create gallery_LL.xml where LL is the language code
        """

        XML=file(op.join(self.dir,"gallery_"+self.lang+".xml"),"w")
        (titre_fr,titre_en)=current_title(self.dir)
        if self.lang=="EN":
            titre=titre_en
        else:
            titre=titre_fr
        XML.writelines( """\
    <?xml version="1.0" encoding="UTF-8"?>
    <simpleviewerGallery maxImageWidth="720" maxImageHeight="576" textColor="0xFFFFFF" frameColor="0xffffff" frameWidth="20" stagePadding="40" thumbnailColumns="3" thumbnailRows="4" navPosition="left" title="%s" enableRightClickOpen="false" backgroundImagePath="" imagePath="images/" thumbPath="thumbs/">
    """%" - ".join(titre))

        for ii in glob.glob(op.join(self.dir,"images","photo*.jpg")):
            i=ii
            XML.writelines("<image>\n")
            XML.writelines("   <filename>%s</filename>\n"%(op.basename(i)))
            text = self.legende(i)
            XML.writelines("  <caption>%s</caption>\n"%(text))
            XML.writelines("</image>\n")
        XML.writelines("</simpleviewerGallery>")
        XML.close()
    def legende(self,image):
        """search and return the legend for image in image dir and in current language
        search either in photoXX_LL.txt
        or in legendes_LL.txt"""
        f1 =  image.replace(".jpg","_"+self.lang+".txt")
        f2 =  op.join(op.dirname(image),"legendes_"+self.lang+".txt")
        try:
            f=file(f1)
            text=" ".join(f.readlines()).strip(" \n")
            f.close()
        except:
            text = ""
        if text == "":
            prefix = op.basename(image).replace(".jpg"," : ")   # photoxx : 
            try:
                f=file(f2)
                for l in f:
                    if l.startswith(prefix):
                        text = l.replace(prefix,"")
                        break
                f.close()
            except:
                text = ""
        if text == "":
            print "pas de légende en %s pour %s dans %s "%(self.lang,image,op.abspath(self.dir))
        return text

    def do_html(self,lang="FR"):
        """docstring for do_html"""
        formvar={}
        formvar["link"]=self.link
        formvar["mois"]=self.nomMois
        formvar["annee"]=self.annee
        formvar["lang"]=self.lang
        formvar["flat_title"]=" - ".join(self.titre)
        formvar["br_titre"]="<br>".join(self.titre)
        HTML=file(op.join(self.dir,self.diaponame),"w")
        HTML.writelines(self.texte%formvar)
        HTML.close()

class presentation:
    """permet de créer des page de presentation"""
    def __init__(self, dir,lang="FR"):
        self.dir = dir
        (self.annee,self.mois)=current_date(self.dir)
        self.setLang(lang)
        self.texte="""\
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<title>%(flat_title)s</title>
<link href="/css/nfg.css" type="text/css" media="screen" rel="stylesheet">
<link rel="shortcut icon" type="image/x-icon" href="/images/favicon.ico">
<script language="JavaScript">
<!--
function openWindow(url,name)
{ popupWin = window.open(url,name,'resizable, scrollbars, width=850,height=300')
}
// -->
</script>
</head>
<body>
<a href="/"><img id="logo" border="0" src="/images/logo_FOI.gif" alt="Logo" border="0" title="Réseau NetForGod"></a>
<img id="header" src="/images/bande-800-s.jpg" alt="header">
<div id="bandeau">
<div class="bd-gauche">
 <a id="ccn" href="http://www.chemin-neuf.org"><img src="/images/logo_k4.gif" height="35" border="0" alt="Logo Communaute du Chemin-neuf" title="Communauté du Chemin-Neuf"></a>
        %(slogan)s 
    </div>
    <div class="bd-droit">    %(link)s    </div>
</div>
<div id="page-centree" style="font-size: 16px">
<IMG alt="affiche" src="affiche.jpg" border="0" width="640" height="480">
%(resume)s
%(diapo)s
<hr width="30%%">
<a style="font-size: 16px" href="/media/frat.html">%(discover)s</A> <br>
<hr width="30%%">
"""+footer

    def setLang(self,lang):
        """docstring for setLang"""
        self.lang=lang
        (titre_fr,titre_en)=current_title(self.dir)
        (annee,mois)=current_date(self.dir)
        if self.lang=="FR":
            self.slogan="Au service de l'UNITÉ des CHRÉTIENS et de la PAIX dans le MONDE."
            self.discover="Découvir la fraternité NetForGod"
            self.presname="presentation.html"
            self.diaponame="diaporama.html"
            self.resname="resume.html"
            self.resume="Résumé du film"
            self.titre=titre_fr
            self.nomMois=langues.mois_nom[self.mois]
            self.link="""Français<a href="presentation_EN.html"> / English</a>"""
        elif self.lang=="EN":
            self.slogan="Working for Christian unity and for peace in the world !"
            self.discover="Discover the NetForGod fraternity"
            self.presname="presentation_EN.html"
            self.diaponame="diaporama_EN.html"
            self.resname="resume_EN.html"
            self.resume="Movie synopsis"
            self.titre=titre_en
            self.nomMois=langues.month_name[self.mois]
            self.link="""English <a href="presentation.html">/ Français</a>"""
    
    def do_html(self,lang="FR"):
        """docstring for do_html"""
        formvar={}
        formvar["link"]=self.link
        formvar["mois"]=self.nomMois
        formvar["annee"]=self.annee
        formvar["slogan"]=self.slogan
        formvar["discover"]=self.discover
        formvar["lang"]=self.lang
        formvar["flat_title"]=" - ".join(self.titre)
        hr=0
        if op.exists(op.join(self.dir,self.resname)):
            formvar["resume"]="""<hr width="30%%"><a style="font-size: 16px" href="javascript:openWindow('%s','%s')">%s</A> <br>"""%(self.resname,self.resume,self.resume)
            hr=1
        else:
            formvar["resume"]=''
        if op.exists(op.join(self.dir,self.diaponame)):
            if hr==0:
                hr='<hr width="30%%">'
            else:
                hr=''
            formvar["diapo"]='%s<a style="font-size: 16px" href="%s">%s</A> <br>'%(hr,self.diaponame,"Diaporama")
        else:
            formvar["diapo"]=''
        HTML=file(op.join(self.dir,self.presname),"w")
        HTML.writelines(self.texte%formvar)
        HTML.close()


class resume:
    """permet de créer des pages de resume"""
    def __init__(self, dir,lang="FR"):
        self.dir = dir
        imlist = glob.glob(op.join(self.dir,"textes","resume_*.txt"))
        self.empty = len(imlist)==0 # tells that there is no resume available
        self.setLang(lang)
        self.texte="""\
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
	<meta http-equiv="Content-type" content="text/html; charset=utf-8">
	<link rel="stylesheet" href="/css/nfg.css" type="text/css" media="screen" title="no title" charset="utf-8">
</head>
<body>
<div id="page-centree">
<H1>%(resume)s</H1>
<p>%(resume_text)s</p>
</div>
<input type=button value="Fermer cette fenêtre" onClick="javascript:window.close();">
</body></html>
"""
    def setLang(self,lang):
        """docstring for setLang"""
        self.lang=lang
        (resume_fr,resume_en)=current_resume(self.dir)
        if self.lang=="FR":
            self.slogan="Au service de l'UNITÉ des CHRÉTIENS et de la PAIX dans le MONDE."
            self.discover="Découvir la fraternité NetForGod"
            self.presname="presentation.html"
            self.diaponame="diaporama.html"
            self.resname="resume.html"
            self.resume="Résumé du film"
            self.resume_text=resume_fr
        elif self.lang=="EN":
            self.slogan="Working for Christian unity and for peace in the world !"
            self.discover="Discover the NetForGod fraternity"
            self.presname="presentation_EN.html"
            self.diaponame="diaporama_EN.html"
            self.resname="resume_EN.html"
            self.resume="Movie synopsis"
            self.resume_text=resume_en
    
    def do_html(self,lang="FR"):
        """docstring for do_html"""
        formvar={}
        formvar["resume"]=self.resume
        formvar["resume_text"]="<br>".join(self.resume_text)
        HTML=file(op.join(self.dir,self.resname),"w")
        HTML.writelines(self.texte%formvar)
        HTML.close()


class video:
    """
    permet de créer des pages video pour chaque film (celle qui présente le film en flash)
    Cette page minimise l'utilisation du javascript, et donne accès à l'achat de la video.
    """
    def __init__(self, dir,lang="FR"):
        self.dir = dir
        imlist = glob.glob(op.join(self.dir,"textes","resume_*.txt"))
        self.empty = len(imlist)==0 # tells that there is no resume available
        (self.annee,self.mois)=current_date(self.dir)
        self.setLang(lang)
        self.texte="""\
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<title>%(flat_title)s</title>
<link href="/css/nfg.css" type="text/css" media="screen" rel="stylesheet">
<link rel="shortcut icon" type="image/x-icon" href="/images/favicon.ico">
<script language="JavaScript">
<!--
function openWindow(url,name)
{ popupWin = window.open(url,name,'resizable, scrollbars, width=850,height=300')
}
// -->
</script>
</head>
<body>
<a href="/"><img id="logo" border="0" src="/images/logo_FOI.gif" alt="Logo" border="0" title="Réseau NetForGod"></a>
<img id="header" src="/images/bande-800-s.jpg" alt="header">
<div id="bandeau">
<div class="bd-gauche">
 <a id="ccn" href="http://www.chemin-neuf.org"><img src="/images/logo_k4.gif" height="35" border="0" alt="Logo Communaute du Chemin-neuf" title="Communauté du Chemin-Neuf"></a>
%(slogan)s 
</div>
<div class="bd-droit">    %(link)s    </div>
</div>
<div id="page-centree" style="font-size: 16px">
<object type="application/x-shockwave-flash" width="352" height="288" wmode="transparent" data="/js/flvplayer.swf?file=%(file)s&amp;showdigits=true">
<param name="movie" value="/js/flvplayer.swf?file=%(file)s&amp;showdigits=true" />
<param name="wmode" value="transparent"/>
</object>
%(resume)s
%(diapo)s
<hr width="30%%">
<a style="font-size: 16px" href="/media/frat.html">%(discover)s</A> <br>
<hr width="30%%">
<BR CLEAR=ALL>
<div id="pied">
<ul>
"""+footer
    def setLang(self,lang):
        """docstring for setLang"""
        self.lang=lang
        (titre_fr,titre_en)=current_title(self.dir)
        (annee,mois)=current_date(self.dir)
        if self.lang=="FR":
            self.slogan="Au service de l'UNITÉ des CHRÉTIENS et de la PAIX dans le MONDE."
            self.discover="Découvir la fraternité NetForGod"
            self.presname="presentation.html"
            self.diaponame="diaporama.html"
            self.resname="resume.html"
            self.videoname="video.html"
            self.resume="Résumé du film"
            self.titre=titre_fr
            self.nomMois=langues.mois_nom[self.mois]
            self.link="""Français<a href="presentation_EN.html"> / English</a>"""
        elif self.lang=="EN":
            self.slogan="Working for Christian unity and for peace in the world !"
            self.discover="Discover the NetForGod fraternity"
            self.presname="presentation_EN.html"
            self.diaponame="diaporama_EN.html"
            self.resname="resume_EN.html"
            self.videoname="video_EN.html"
            self.resume="Movie synopsis"
            self.titre=titre_en
            self.nomMois=langues.month_name[self.mois]
            self.link="""English <a href="presentation.html">/ Français</a>"""

    
    def do_html(self,lang="FR"):
        """docstring for do_html"""
        formvar={}
        formvar["link"]=self.link
        formvar["mois"]=self.nomMois
        formvar["annee"]=self.annee
        formvar["slogan"]=self.slogan
        formvar["discover"]=self.discover
        formvar["lang"]=self.lang
        formvar["flat_title"]=" - ".join(self.titre)
        formvar["file"]="test.flv"
        HTML=file(op.join(self.dir,self.videoname),"w")
        HTML.writelines(self.texte%formvar)
        HTML.close()

###################################################################################

class VodPage:
    """ Cette classe construit les pages principales de VOD """
    def __init__(self, config, langue="FR"):
        self.langue=langue
        self.config = config
        self.debug = config.debug
        self.dir = config.video_dir
        self.TmplDir = config.TmplDir
        self.flv_list = self.do_flv_list()
        self.titre_list = self.do_titre_list()
        self.langues_list = self.do_lang_list()
        self.resum_list = self.do_resum_list()
        self.diapo_list = self.do_diapo_list()

    def html_base_liste(self):
        """charge la base de la page html pour le VOD en mode liste"""
        if (self.langue == "FR"):
            VOD=file(op.join(self.TmplDir, "vod_list_fr.html"))
            r = "".join(VOD.readlines())
            VOD.close()
        else:
            VOD=file(op.join(self.TmplDir, "vod_list_en.html"))
            r = "".join(VOD.readlines())
            VOD.close()
        return r

    def html_base_vod(self):
        """charge la base de la page html pour le VOD."""
# base html de la page -  2 versions _fr et _en - les champs %s sont remplacés au moment de l'utilisation
        if (self.langue == "FR"):
            VOD=file(op.join(self.TmplDir,"vod_fr.html"))
            r = "".join(VOD.readlines())
            VOD.close()
        else:
            VOD=file(op.join(self.TmplDir,"vod_en.html"))
            r = "".join(VOD.readlines())
            VOD.close()
        return r
    ###################################################################################
    def vod_html(self):
        """ cree la page html VOD dans la langue cible"""
        # calcule toutes les parties variables
        flv = str(self.flv_list).replace('[','').replace(']','')
        titre = ""
        for i in self.titre_list:
            if titre == "":
                titre = "'" + i + "'"
            else:
                titre = titre + ", '" + i + "'"
        langs = repr(self.langues_list).replace('[','').replace(']','')
        if self.langue == "FR":
            autrepage = self.config.page_name_en
        else:
            autrepage = self.config.page_name
        video_du_mois = self.do_mois()
        table_video = self.do_emisions()
        Ares = repr(self.resum_list).replace('[','').replace(']','') 
        Adia = repr(self.diapo_list).replace('[','').replace(']','')
        Adur = []
        debit = 1100
        for i in self.flv_list:
            dur = op.getsize(op.join(self.dir,i,"FR_divx.avi"))
            dur = round(dur*8/debit/60/1024)
            if self.debug: print i,dur," min"
            Adur.append(dur)
        
        # et colle le dans le html grace à vars qui retourne un dico des var locales
        return (self.html_base_vod() % vars())

    ###################################################################################
    def liste_html(self):
        """ cree la page html VOD mode liste dans la langue cible"""
        # calcul toutes les parties variables
        flv = str(self.flv_list).replace('[','').replace(']','')
        titre = ""
        for i in self.titre_list:
            if titre == "":
                titre = "'" + i + "'"
            else:
                titre = titre + ", '" + i + "'"
        langs = repr(self.langues_list).replace('[','').replace(']','')
        if self.langue == "FR":
            autrepage = self.config.liste_name_en
        else:
            autrepage = self.config.liste_name
        liste_video = self.do_liste_emmission()
        # et colle le dans le html grace à vars qui retourne un dico des var locales
        return (self.html_base_liste() % vars())

    ###################################################################################
    def do_flv_list(self):
        """ fabrique la liste des flv dans la langue cible
        cherche dans tous les sous-dossiers de self.dir, un fichier XX_divx.flv
        si le dossier contient un fichier au nom de public, alors l'entrée est rajoutée
        au passage, crée tous les liens entre self.dir (là où sont vraiment les video) et working_dir (là où sont les pages de visu)
        retourne la liste des dossiers rajoutés dans working_dir
        l'ordre de Cette liste determine l'ordre des videos - par defaut c'est l'ordre anti alphabetique
        si un dossier contient un fichier (vide) "premier" alors il est mis en tete
        """
        try:
            motif = self.langue+"_divx.flv"
        except:
            motif = "FR_divx.flv"
        l1=[]
        prem = ""
        for dir in glob.glob(op.join(self.dir,"*")): # pour tout les directory
            if op.isdir(dir):  
                if op.isfile(op.join(dir,"public")) and op.isfile(op.join(dir,motif)):   # qui contiennent le fichier "public" et contient au moins une video
                    if self.debug : print dir
                    new_dir = self.makelink(dir, self.config.working_dir)
                    l1.append(op.basename(new_dir))
                    if op.isfile(op.join(dir,"premier")):
                        prem = op.basename(new_dir)
        l1.sort()
        l1.reverse()
        if prem:
            l1.remove(prem)
            l1.insert(0,prem)
        # lien permanent vers le film du mois
        actuel = op.join(self.config.working_dir,"actuel")
        try:
            os.remove(actuel)
        except:
            pass
        os.symlink ( op.join(self.config.working_dir,l1[0]), actuel)
        if self.debug: print "flv_list", l1
        return (l1)
    
    ###################################################################################
    def makelink(self,source,cible):
        """s'assure que tout les liens entres les dossiers source (video) et cible (VOD) sont là"""
        # source : self.dir/MyMovie   -  cible : VOD   -  dir : VOD/MyMovie
        dir = op.join(cible,op.basename(source))
        # create dir
        if not op.isdir(dir):
            os.mkdir(dir)
        # link flvs
        for flv in glob.glob(source+"/*.flv"):
            new_flv=op.join(dir,op.basename(flv))
            if not op.islink(new_flv):
                print "LINK", flv, new_flv
                try: 
                    os.symlink(flv, new_flv)
                except:
                    raise "Probleme avec ln -s %s %s"%(flv, new_flv)
        # affiche, textes, images
        for F in ("affiche.jpg", "textes", "images", "thumbs", "presentation.html","presentation_EN.html","diaporama.html","diaporama_FR.html","diaporama_EN.html","resume.html","resume_FR.html","resume_EN.html","gallery_EN.xml","gallery_FR.xml"):
            old_F=op.join(source,F)
            new_F=op.join(self.config.working_dir,dir,F)
            if not op.islink(new_F) and op.exists(old_F):
                print "LINK", old_F, new_F
                try:
                    os.symlink(old_F, new_F)
                except:
                    print "probleme avec ln -s %s %s"%(old_F, new_F)
        return dir

    ###################################################################################
    def strip_flv(self,l):
        """ reformate un flv, pour ne garder que la base des noms
        i.e. FOI_06_07/FR_divx.flv => FOI_06_07
        plus utilisé
        """
#        motif = "_"+self.langue+"_"
        motif = "_FR_"
        l2 = l.replace(motif + "divx.flv","")
        return( op.basename(l2) )
    
    ###################################################################################
    def do_titre_list(self):
        """ fabrique la liste des titre dans la langue cible"""
        t = []
        for i in self.flv_list:
            try:
                f=file ( op.join( i, "textes", "titre_" + self.langue + ".txt"))
                tx = clean(f.read())
                t.append(tx)
                f.close()
            except:
                t.append("--")
        return (t)
    
    ###################################################################################
    def do_lang_list(self):
        """ fabrique la liste des langues pour chaque video trouvée"""
        l = []  # pour chaque entrée
        for base in self.flv_list:
            f = glob.glob( op.join(base,"*divx.flv"))
            ll = ""     # liste des langues pour chaque entrée
            for j in langues.ordrelangues.split():    # sur toutes les langues
                for k in f:     # sur tous les fichiers
                    try:
                        [ll1] = re.findall("([A-Z][A-Z]+)_divx",  k)
                        if j == ll1:
                            if ll=="":
                                ll=ll1
                            else:
                                ll = ll+" "+ll1
                    except:
                        if self.debug: print "langue inconnue: ",k
            l.append(ll)
        return(l)
    ###################################################################################
    def do_resum_list(self):
        """fabrique un tableau de test (0/1) pour la présence d'un résumé """
        l = []  # pour chaque entrée
        for base in self.flv_list:
            if op.exists(op.join(base,"textes/resume_FR.txt")):
                l.append(1)
            else:
                l.append(0)
        return(l)
    ###################################################################################
    def do_diapo_list(self):
        """fabrique un tableau de test (0/1) pour la présence d'un diaporama """
        l = []  # pour chaque entrée
        for base in self.flv_list:
            if op.exists(op.join(base,"diaporama.html")):
                l.append(1)
            else:
                l.append(0)
        return(l)
    
    ###################################################################################
    def do_emisions(self):
        """ fabrique la table des emissions précédentes pour la page VOD"""
        tabl = ""
        cote="g"    # cote alterne g / d pour faire le tableau
        if len(self.flv_list)>1:        # tout sauf la dernière qui est à part
            liste = self.flv_list[1:]
            index=1
        else:
            liste=self.flv_list
            index=0
        for i in liste:
            index_em=index
            index +=1
            (titre,affiche,date) = self.do_ti_aff_date(i)
    # base html de la case pour une emission
            if index<6:
                emision_fr = """<span class="tdemission%s"><a href="#" onclick="javascript:PresMois(%d)"><img border="0" class="affiche-2" alt="affiche" src="%s"/><br clear="all"/><span class="titre"> %s </span></a></span>\n""" % (cote,index_em, affiche,titre)
            else:
                emision_fr = """<span class="tdemission%s_sm"><a href="#" onclick="javascript:PresMois(%d)"><span class="titre"> %s </span></a></span>\n""" % (cote,index_em,titre)
            if (cote == "g"):
                cote = "d"
            else:
                cote = "g"
            tabl = tabl + emision_fr
        if (cote == "d"):
            tabl = tabl+"""<span class="tdemissiond_sm">&nbsp;</span>\n"""
        return (tabl)
    ###################################################################################
    def do_liste_emmission(self):
        """ fabrique la table des emissions précédentes pour la page liste """
        texte=""
        # base html de la case pour une emission
        base="""
        <div class="ltfilm">
        <a href="/s/%(perm)s?dt=%(dt)s&amp;lg=%(langue)s"><img border="0" class="affiche-2" alt="affiche" src="%(affiche)s"/></a>
        <p class="date-lt">%(date)s</p>
        <p class="lttitre">%(titre)s</p>
        </div>
        """
        texte=""
        for dir in self.flv_list:
            (titre,affiche,date) = self.do_ti_aff_date(dir)
            [(dt)] = re.findall("FOI_(\d\d_\d\d)",dir)
            langue = self.langue
            if self.langue == "FR":
                perm = "perm.php"
            else:
                perm = "permn.php"
            texte=texte+base % vars()
        return (texte)
    
    ###################################################################################
    def do_mois(self):
        """ fabrique la presentation du mois courant """
        i=self.flv_list[0]
        (titre,affiche,date) = self.do_ti_aff_date(i)
        mois = """<p class="titre-mois"> %s </p><div class="aff-mois"><a href="#" onclick="javascript:PresMois(0)">
                 <img border="0" class="affiche-1" alt="affiche" src="%s"/></a></div>
                 <div class="texte-mois"> </div>""" % (titre, affiche)
        return(mois)
    
    ###################################################################################
    def do_ti_aff_date(self,dirb):
        """utilitaire pour calculer le nom et le titre"""
        try:
            f = file(  op.join(dirb, "textes", "titre_" + self.langue + ".txt"))
            titre = clean(f.read())
            f.close()
        except:
            titre="<br/>"
        affiche = op.join(dirb, "affiche.jpg")
        if not op.isfile(affiche):
            affiche = "/images/affiche.gif"
        try:
            [(annee,mois)] = re.findall("FOI_(\d\d)_(\d\d)",dirb)
            if (self.langue == "FR"):
                # if mois in ("04","08","10"):    # avril aout octobre
                #     date = "La vidéo du mois d'%s %i"%(langues.mois_nom[int(mois)],int(annee)+2000)
                # else:
                #     date = "La vidéo du mois de %s %i"%(langues.mois_nom[int(mois)],int(annee)+2000)
                date = "%s %i"%(langues.mois_nom[int(mois)],int(annee)+2000)
            if (self.langue == "EN"):
            #     date = "%s %i video"%(langues.month_name[int(mois)],int(annee)+2000)
                date = "%s %i"%(langues.month_name[int(mois)],int(annee)+2000)
        except:
            date = " "
        return ((titre,affiche,date))

if __name__ == "main":
    print "cette bibliothèque doit être importée pour être utilisée"

